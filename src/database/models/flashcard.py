from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base


class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    deck_id = Column(Integer, ForeignKey("decks.id", ondelete="CASCADE"), nullable=False)
    word = Column(String, nullable=False)
    pinyin = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    example_sentence = Column(String, nullable=True)  # nullable=True since it's optional

    # Relationship to Deck
    deck = relationship("Deck", back_populates="flashcards")
