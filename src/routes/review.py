from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from src.database.db import SessionLocal
from src.database.models import deck
from src.database.models.deck import Deck
from src.database.models.flashcard import Flashcard
from src.database.models.review import CardReview
from datetime import datetime, timedelta
import random

review_bp = Blueprint('review', __name__)


def calculate_next_interval(current_interval, was_correct):
    """
    Calculate the next review interval using a simple spaced repetition algorithm
    """
    if was_correct:
        # If correct, double the interval (exponential increase)
        return min(current_interval * 2, 30)  # Cap at 30 days
    else:
        # If wrong, reset to 1 day
        return 1


@review_bp.route('/review/<int:deck_id>')
def start_review(deck_id):
    db = SessionLocal()
    try:
        deck = db.query(Deck).get(deck_id)
        if not deck:
            return "Deck not found", 404

        # Get cards that are due for review
        current_time = datetime.utcnow()
        flashcards = db.query(Flashcard) \
            .filter(Flashcard.deck_id == deck_id) \
            .filter(Flashcard.next_review <= current_time) \
            .all()

        if not flashcards:
            return render_template('no_reviews.html', deck=deck)

        # Shuffle the flashcards
        random.shuffle(flashcards)

        # Store the flashcard IDs in the session for review
        session['cards_to_review'] = [card.id for card in flashcards]
        session['current_card_index'] = 0

        return render_template('review.html',
                               deck=deck,
                               card=flashcards[0],
                               current_card_index=0,
                               progress=0,
                               total=len(flashcards))
    finally:
        db.close()


@review_bp.route('/review/<int:deck_id>/submit/<int:card_id>', methods=['POST'])
def submit_review(deck_id, card_id):
    if 'cards_to_review' not in session:
        return redirect(url_for('review.start_review', deck_id=deck_id))

    rating = request.form.get('rating')
    was_correct = rating == 'correct'

    db = SessionLocal()
    try:
        card = db.query(Flashcard).get(card_id)
        if not card:
            abort(404)

        # Get the current interval (or use 1 if it's the first review)
        current_interval = 1
        last_review = db.query(CardReview) \
            .filter(CardReview.card_id == card_id) \
            .order_by(CardReview.reviewed_at.desc()) \
            .first()

        if last_review:
            current_interval = last_review.next_interval

        # Calculate next interval
        next_interval = calculate_next_interval(current_interval, was_correct)
        next_review_date = datetime.utcnow() + timedelta(days=next_interval)

        # Create review record
        review = CardReview(
            card_id=card_id,
            correct=was_correct,
            next_interval=next_interval,
            next_review=next_review_date
        )
        db.add(review)

        # Update card's next review date
        card.next_review = next_review_date

        db.commit()

        # Move to next card
        current_index = session['current_card_index'] + 1
        total_cards = len(session['cards_to_review'])

        if current_index >= total_cards:
            session.pop('cards_to_review', None)
            session.pop('current_card_index', None)
            return redirect(url_for('decks.view_deck', deck_id=deck_id))

        # Get the next card
        next_card_id = session['cards_to_review'][current_index]
        next_card = db.query(Flashcard).get(next_card_id)

        # Update the session
        session['current_card_index'] = current_index

        # Calculate progress
        progress = (current_index / total_cards) * 100

        return render_template('review.html',
                               deck=deck,
                               card=next_card,
                               current_card_index=current_index,
                               progress=progress,
                               total=total_cards)
    finally:
        db.close()
