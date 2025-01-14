from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from src.database.db import get_db
from src.database.models import Deck, Flashcard

# Define the blueprint for deck routes
decks_bp = Blueprint("decks", __name__, url_prefix="/decks")

# Redirect root /decks to /decks/view
@decks_bp.route("/", methods=["GET"])
def index():
    if request.headers.get('Accept') == 'application/json':
        # If API request, return JSON
        return get_decks_json()
    # Otherwise redirect to HTML view
    return redirect(url_for('decks.view_decks'))

# HTML Routes
@decks_bp.route("/view", methods=["GET"])
def view_decks():
    db = next(get_db())
    try:
        decks = db.query(Deck).all()
        return render_template('decks.html', decks=decks)
    finally:
        db.close()

@decks_bp.route("/view/<int:deck_id>", methods=["GET"])
def view_deck(deck_id):
    db = next(get_db())
    try:
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if not deck:
            abort(404, description="Deck not found")
        return render_template('deck_detail.html', deck=deck)
    finally:
        db.close()

@decks_bp.route('/deck/<int:deck_id>/card/add', methods=['GET', 'POST'])
def add_card(deck_id):
    db = next(get_db())
    try:
        deck = db.query(Deck).get(deck_id)
        if not deck:
            return "Deck not found", 404

        if request.method == 'POST':
            new_card = Flashcard(
                word=request.form['word'],
                pinyin=request.form['pinyin'],
                translation=request.form['translation'],
                example_sentence=request.form['example_sentence'],
                deck_id=deck_id
            )
            db.add(new_card)
            db.commit()
            flash('Card added successfully!', 'success')
            return redirect(url_for('decks.view_deck', deck_id=deck_id))

        return render_template('add_card.html', deck=deck)
    finally:
        db.close()

@decks_bp.route('/deck/<int:deck_id>/card/<int:card_id>/edit', methods=['GET', 'POST'])
def edit_card(deck_id, card_id):
    db = next(get_db())
    try:
        card = db.query(Flashcard).get(card_id)
        if not card:
            return "Card not found", 404

        if request.method == 'POST':
            card.word = request.form['word']
            card.pinyin = request.form['pinyin']
            card.translation = request.form['translation']
            card.example_sentence = request.form['example_sentence']
            db.commit()
            flash('Card updated successfully!', 'success')
            return redirect(url_for('decks.view_deck', deck_id=deck_id))

        return render_template('edit_card.html', card=card, deck_id=deck_id)
    finally:
        db.close()

@decks_bp.route('/deck/<int:deck_id>/card/<int:card_id>/delete', methods=['POST'])
def delete_card(deck_id, card_id):
    db = next(get_db())
    try:
        card = db.query(Flashcard).get(card_id)
        if card:
            db.delete(card)
            db.commit()
            flash('Card deleted successfully!', 'success')
        return redirect(url_for('decks.view_deck', deck_id=deck_id))
    finally:
        db.close()

# API Routes
@decks_bp.route("/api/decks", methods=["GET"])
def get_decks_json():
    db = next(get_db())
    try:
        decks = db.query(Deck).all()
        return jsonify([{"id": deck.id, "name": deck.name, "description": deck.description} for deck in decks])
    finally:
        db.close()

@decks_bp.route("/api/decks/<int:deck_id>", methods=["GET"])
def get_deck_json(deck_id):
    db = next(get_db())
    try:
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if not deck:
            abort(404, description="Deck not found")
        return jsonify({"id": deck.id, "name": deck.name, "description": deck.description})
    finally:
        db.close()

@decks_bp.route("/api/decks", methods=["POST"])
def create_deck():
    db = next(get_db())
    try:
        data = request.json
        if not data or "name" not in data:
            abort(400, description="Missing required fields: name")

        new_deck = Deck(name=data["name"], description=data.get("description"))
        db.add(new_deck)
        db.commit()
        return jsonify({"id": new_deck.id, "name": new_deck.name, "description": new_deck.description}), 201
    except IntegrityError:
        db.rollback()
        abort(400, description="Deck with the same name already exists")
    finally:
        db.close()

@decks_bp.route("/api/decks/<int:deck_id>", methods=["PUT"])
def update_deck(deck_id):
    db = next(get_db())
    try:
        data = request.json
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if not deck:
            abort(404, description="Deck not found")

        deck.name = data.get("name", deck.name)
        deck.description = data.get("description", deck.description)
        db.commit()
        return jsonify({"id": deck.id, "name": deck.name, "description": deck.description})
    finally:
        db.close()

@decks_bp.route("/api/decks/<int:deck_id>", methods=["DELETE"])
def delete_deck(deck_id):
    db = next(get_db())
    try:
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if not deck:
            abort(404, description="Deck not found")

        db.delete(deck)
        db.commit()
        return jsonify({"message": f"Deck {deck_id} deleted successfully"}), 200
    finally:
        db.close()
