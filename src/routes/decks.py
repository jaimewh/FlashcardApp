from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from src.database.db import get_db
from src.database.models.deck import Deck

# Define the blueprint for deck routes
decks_bp = Blueprint("decks", __name__, url_prefix="/decks")

@decks_bp.route("/", methods=["GET"])
def get_decks():
    db = next(get_db())
    decks = db.query(Deck).all()
    return jsonify([{"id": deck.id, "name": deck.name, "description": deck.description} for deck in decks])

@decks_bp.route("/<int:deck_id>", methods=["GET"])
def get_deck(deck_id):
    db = next(get_db())
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if not deck:
        abort(404, description="Deck not found")
    return jsonify({"id": deck.id, "name": deck.name, "description": deck.description})

@decks_bp.route("/", methods=["POST"])
def create_deck():
    db = next(get_db())
    data = request.json
    if not data or "name" not in data:
        abort(400, description="Missing required fields: name")

    new_deck = Deck(name=data["name"], description=data.get("description"))
    try:
        db.add(new_deck)
        db.commit()
        return jsonify({"id": new_deck.id, "name": new_deck.name, "description": new_deck.description}), 201
    except IntegrityError:
        db.rollback()
        abort(400, description="Deck with the same name already exists")

@decks_bp.route("/<int:deck_id>", methods=["PUT"])
def update_deck(deck_id):
    db = next(get_db())
    data = request.json
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if not deck:
        abort(404, description="Deck not found")

    deck.name = data.get("name", deck.name)
    deck.description = data.get("description", deck.description)
    db.commit()
    return jsonify({"id": deck.id, "name": deck.name, "description": deck.description})

@decks_bp.route("/<int:deck_id>", methods=["DELETE"])
def delete_deck(deck_id):
    db = next(get_db())
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if not deck:
        abort(404, description="Deck not found")

    db.delete(deck)
    db.commit()
    return jsonify({"message": f"Deck {deck_id} deleted successfully"}), 200