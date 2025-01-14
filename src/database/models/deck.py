from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base

class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # Relationship
    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete-orphan")
