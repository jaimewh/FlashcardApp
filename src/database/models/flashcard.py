from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base
from datetime import datetime

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    pinyin = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    example_sentence = Column(String)
    deck_id = Column(Integer, ForeignKey('decks.id'))
    created_at = Column(DateTime(), default=datetime.utcnow)
    next_review = Column(DateTime(), default=datetime.utcnow)

    # Relationships
    deck = relationship("Deck", back_populates="flashcards")
    reviews = relationship("CardReview", back_populates="card", cascade="all, delete-orphan")
