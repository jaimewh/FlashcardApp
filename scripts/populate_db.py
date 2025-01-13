from sqlalchemy.orm import Session
from src.database.db import SessionLocal
from src.database.models.deck import Deck
from src.database.models.flashcard import Flashcard

# Sample data
DECKS = [
    {"name": "Basic Mandarin", "description": "Common greetings and phrases."},
    {"name": "Food Vocabulary", "description": "Learn Mandarin words for food and dining."},
    {"name": "Travel Phrases", "description": "Essential phrases for traveling in China."},
]

FLASHCARDS = {
    "Basic Mandarin": [
        {"word": "你好", "pinyin": "nǐ hǎo", "translation": "Hello"},
        {"word": "谢谢", "pinyin": "xiè xie", "translation": "Thank you"},
        {"word": "再见", "pinyin": "zài jiàn", "translation": "Goodbye"},
    ],
    "Food Vocabulary": [
        {"word": "苹果", "pinyin": "píng guǒ", "translation": "Apple"},
        {"word": "米饭", "pinyin": "mǐ fàn", "translation": "Rice"},
        {"word": "茶", "pinyin": "chá", "translation": "Tea"},
    ],
    "Travel Phrases": [
        {"word": "机场", "pinyin": "jī chǎng", "translation": "Airport"},
        {"word": "火车站", "pinyin": "huǒ chē zhàn", "translation": "Train station"},
        {"word": "酒店", "pinyin": "jiǔ diàn", "translation": "Hotel"},
    ],
}

# Function to populate the database
def populate_database():
    db = SessionLocal()
    try:
        # Add decks
        for deck_data in DECKS:
            deck = Deck(name=deck_data["name"], description=deck_data["description"])
            db.add(deck)
            db.commit()
            db.refresh(deck)

            # Add flashcards to the deck
            for flashcard_data in FLASHCARDS.get(deck.name, []):
                flashcard = Flashcard(
                    deck_id=deck.id,
                    word=flashcard_data["word"],
                    pinyin=flashcard_data["pinyin"],
                    translation=flashcard_data["translation"],
                )
                db.add(flashcard)

        # Commit all changes
        db.commit()
        print("Database populated successfully!")
    except Exception as e:
        print(f"Error populating database: {e}")
        db.rollback()
    finally:
        db.close()

# Run the script
if __name__ == "__main__":
    populate_database()
