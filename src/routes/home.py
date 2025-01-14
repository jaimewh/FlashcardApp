from flask import Blueprint, render_template
from src.database.db import Session
from src.database.models.deck import Deck  # Assuming you have a Deck model

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    db = Session()
    try:
        # Get some basic stats for the dashboard
        total_decks = db.query(Deck).count()
        recent_decks = db.query(Deck).order_by(Deck.created_at.desc()).limit(5).all()

        return render_template('home.html',
                               total_decks=total_decks,
                               recent_decks=recent_decks)
    finally:
        db.close()


@home_bp.route('/about')
def about():
    return render_template('about.html')
