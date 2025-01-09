from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Flashcard(Base):
    __tablename__ = "flashcards"
    id = Column(Integer, primary_key=True, index=True)
    front = Column(String, nullable=False)  # front
    back = Column(String, nullable=False)   # back
    pronunciation = Column(String, nullable=True)  # pronunciation
    deck_id = Column(Integer, ForeignKey("decks.id", ondelete="CASCADE"), nullable=False)  # Foreign key to Deck

    deck = relationship("Deck", back_populates="flashcards")