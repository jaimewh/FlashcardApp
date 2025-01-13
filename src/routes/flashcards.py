from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src.database.db import SessionLocal
from src.database.models.flashcard import Flashcard
from src.database.models.deck import Deck

# Create a blueprint for flashcard routes
flashcards_bp = Blueprint("flashcards", __name__, url_prefix="/flashcards")

# Dependency: Provide a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to get all flashcards in a specific deck
@flashcards_bp.route("/deck/<int:deck_id>", methods=["GET"])
def get_flashcards(deck_id):
    db = next(get_db())
    flashcards = db.query(Flashcard).filter(Flashcard.deck_id == deck_id).all()
    return jsonify([flashcard.to_dict() for flashcard in flashcards])

# Route to create a new flashcard
@flashcards_bp.route("/", methods=["POST"])
def create_flashcard():
    db = next(get_db())
    data = request.json
    # Check if the deck exists
    deck = db.query(Deck).filter(Deck.id == data["deck_id"]).first()
    if not deck:
        return jsonify({"error": "Deck not found"}), 404

    flashcard = Flashcard(
        deck_id=data["deck_id"],
        word=data["word"],
        pinyin=data["pinyin"],
        translation=data["translation"],
        example_sentence=data.get("example_sentence", ""),
    )
    db.add(flashcard)
    db.commit()
    db.refresh(flashcard)
    return jsonify(flashcard.to_dict()), 201

# Route to update an existing flashcard
@flashcards_bp.route("/<int:flashcard_id>", methods=["PUT"])
def update_flashcard(flashcard_id):
    db = next(get_db())
    data = request.json
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    if not flashcard:
        return jsonify({"error": "Flashcard not found"}), 404

    # Update fields
    flashcard.word = data.get("word", flashcard.word)
    flashcard.pinyin = data.get("pinyin", flashcard.pinyin)
    flashcard.translation = data.get("translation", flashcard.translation)
    flashcard.example_sentence = data.get("example_sentence", flashcard.example_sentence)

    db.commit()
    return jsonify(flashcard.to_dict())

# Route to delete a flashcard
@flashcards_bp.route("/<int:flashcard_id>", methods=["DELETE"])
def delete_flashcard(flashcard_id):
    db = next(get_db())
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    if not flashcard:
        return jsonify({"error": "Flashcard not found"}), 404

    db.delete(flashcard)
    db.commit()
    return jsonify({"message": "Flashcard deleted successfully"}), 200
