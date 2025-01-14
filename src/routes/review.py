from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash
from src.database.db import get_db
from src.database.models import Deck, Flashcard, CardReview
from src.database.models.deck import Deck
from datetime import datetime, timedelta
import random
from sqlalchemy import func

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
    db = next(get_db())
    try:
        deck = db.query(Deck).get(deck_id)
        if not deck:
            return "Deck not found", 404

        # Get all cards in the deck (removed the next_review filter)
        flashcards = db.query(Flashcard) \
            .filter(Flashcard.deck_id == deck_id) \
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

    db = next(get_db())
    try:
        # Get both card and deck at the start
        card = db.query(Flashcard).get(card_id)
        deck = db.query(Deck).get(deck_id)

        if not card or not deck:
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
            return render_template('review_complete.html', deck=deck)

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

@review_bp.route('/review/<int:deck_id>/stats')
def review_stats(deck_id):
    db = next(get_db())
    try:
        deck = db.query(Deck).get(deck_id)
        if not deck:
            return "Deck not found", 404

        cards = db.query(Flashcard) \
            .filter(Flashcard.deck_id == deck_id) \
            .all()

        stats = []
        for card in cards:
            last_review = db.query(CardReview) \
                .filter(CardReview.card_id == card.id) \
                .order_by(CardReview.reviewed_at.desc()) \
                .first()

            stats.append({
                'word': card.word,
                'next_review': card.next_review,
                'last_result': last_review.correct if last_review else None,
                'review_count': db.query(CardReview) \
                    .filter(CardReview.card_id == card.id) \
                    .count()
            })

        return render_template('review_stats.html', deck=deck, stats=stats)
    finally:
        db.close()

@review_bp.route('/all-decks-stats')
def all_decks_stats():
    db = next(get_db())
    try:
        decks = db.query(Deck).all()
        stats = []

        for deck in decks:
            total_cards = db.query(Flashcard).filter(Flashcard.deck_id == deck.id).count()

            reviewed_cards = db.query(func.count(func.distinct(CardReview.card_id))).join(Flashcard).filter(
                Flashcard.deck_id == deck.id).scalar()

            total_reviews = db.query(func.count(CardReview.id)).join(Flashcard).filter(
                Flashcard.deck_id == deck.id).scalar()

            correct_reviews = db.query(func.count(CardReview.id)).join(Flashcard).filter(Flashcard.deck_id == deck.id,
                                                                                         CardReview.correct == 1).scalar()

            accuracy = (correct_reviews / total_reviews * 100) if total_reviews > 0 else 0

            stats.append({
                'deck_name': deck.name,
                'total_cards': total_cards,
                'reviewed_cards': reviewed_cards,
                'total_reviews': total_reviews,
                'accuracy': round(accuracy, 2)
            })

        return render_template('all_decks_stats.html', stats=stats)
    finally:
        db.close()


@review_bp.route('/review-all-due')
def review_all_due():
    db = next(get_db())
    try:
        # Get all due cards across all decks
        due_cards = db.query(Flashcard).filter(Flashcard.next_review <= datetime.utcnow()).all()

        if not due_cards:
            # If no cards are due, redirect to home with a message
            flash('No cards are due for review at this time.', 'info')
            return redirect(url_for('index'))

        # Store the card IDs in the session
        session['review_cards'] = [card.id for card in due_cards]
        session['current_card_index'] = 0
        session['total_cards'] = len(due_cards)

        # Get the first card and its deck
        first_card = due_cards[0]
        deck = db.query(Deck).get(first_card.deck_id)

        progress = 0
        if session['total_cards'] > 0:
            progress = (session['current_card_index'] / session['total_cards']) * 100

        return render_template('review.html',
                               card=first_card,
                               deck=deck,
                               current_card_index=session['current_card_index'],
                               total=session['total_cards'],
                               progress=progress)
    finally:
        db.close()


@review_bp.route('/submit-all-review/<int:card_id>', methods=['POST'])
def submit_all_review(card_id):
    if 'review_cards' not in session:
        flash('No review session in progress.', 'error')
        return redirect(url_for('index'))

    db = next(get_db())
    try:
        card = db.query(Flashcard).get(card_id)
        if not card:
            flash('Card not found.', 'error')
            return redirect(url_for('index'))

        rating = request.form.get('rating')
        was_correct = rating == 'correct'

        # Get the current interval (days until next review)
        current_interval = 1  # Default to 1 day if no previous reviews
        last_review = db.query(CardReview).filter_by(card_id=card.id).order_by(CardReview.reviewed_at.desc()).first()
        if last_review:
            # Calculate the interval from the last review
            current_interval = (last_review.next_review - last_review.reviewed_at).days

        # Calculate the next interval
        next_interval = calculate_next_interval(current_interval, was_correct)
        next_review_date = datetime.utcnow() + timedelta(days=next_interval)

        # Create a new review record
        review = CardReview(
            card_id=card.id,
            correct=1 if was_correct else 0,
            reviewed_at=datetime.utcnow(),
            next_review=next_review_date,
            next_interval=next_interval
        )
        db.add(review)

        # Update the card's next review date
        card.next_review = next_review_date

        db.commit()

        session['current_card_index'] += 1

        # Check if we've reviewed all cards
        if session['current_card_index'] >= session['total_cards']:
            # Clear session data
            session.pop('review_cards')
            session.pop('current_card_index')
            session.pop('total_cards')
            flash('Review session complete!', 'success')
            return redirect(url_for('index'))

        # Get the next card
        next_card_id = session['review_cards'][session['current_card_index']]
        next_card = db.query(Flashcard).get(next_card_id)
        deck = db.query(Deck).get(next_card.deck_id)

        progress = (session['current_card_index'] / session['total_cards']) * 100

        return render_template('review.html',
                               card=next_card,
                               deck=deck,
                               current_card_index=session['current_card_index'],
                               total=session['total_cards'],
                               progress=progress)
    finally:
        db.close()