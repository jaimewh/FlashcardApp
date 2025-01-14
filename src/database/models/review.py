from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.database.db import Base

class CardReview(Base):
    __tablename__ = "card_reviews"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('flashcards.id'))
    reviewed_at = Column(DateTime, default=datetime.utcnow)
    correct = Column(Boolean, nullable=False)
    # Interval in days until next review
    next_interval = Column(Integer, default=1)
    # Next review date
    next_review = Column(DateTime)

    # Relationship
    card = relationship("Flashcard", back_populates="reviews")
