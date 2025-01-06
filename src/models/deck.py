from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete")