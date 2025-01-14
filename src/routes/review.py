from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from src.database.db import SessionLocal
from src.database.models.deck import Deck
from src.database.models.flashcard import Flashcard
import random

review_bp = Blueprint('review', __name__)


@review_bp.route('/review/<int:deck_id>')
def start_review(deck_id):
    db = SessionLocal()
    try:
        deck = db.query(Deck).get(deck_id)
        if not deck:
            return "Deck not found", 404

        # Get all flashcards from the deck
        flashcards = db.query(Flashcard).filter_by(deck_id=deck_id).all()
        if not flashcards:
            return "No flashcards in this deck", 404

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

@review_bp.route('/review/<int:deck_id>/next', methods=['POST'])
def next_card(deck_id):
    if 'cards_to_review' not in session:
        return redirect(url_for('review.start_review', deck_id=deck_id))

    db = SessionLocal()
    try:
        current_index = session['current_card_index'] + 1
        total_cards = len(session['cards_to_review'])

        # Check if we're done with all cards
        if current_index >= total_cards:
            session.pop('cards_to_review', None)
            session.pop('current_card_index', None)
            return redirect(url_for('decks.view_deck', deck_id=deck_id))

        # Get the next card
        next_card_id = session['cards_to_review'][current_index]
        card = db.query(Flashcard).get(next_card_id)
        deck = db.query(Deck).get(deck_id)

        # Update the session
        session['current_card_index'] = current_index

        # Calculate progress
        progress = (current_index / total_cards) * 100

        return render_template('review.html',
                               deck=deck,
                               card=card,
                               current_card_index=current_index,
                               progress=progress,
                               total=total_cards)
    finally:
        db.close()
