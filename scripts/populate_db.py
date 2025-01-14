import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database.db import engine, Base, SessionLocal
from src.database.models import Deck, Flashcard, CardReview


def populate_database():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Create decks
        basic_deck = Deck(
            name="Basic Mandarin",
            description="Essential everyday Mandarin vocabulary and greetings"
        )

        numbers_deck = Deck(
            name="Numbers & Time",
            description="Numbers, dates, and time-related vocabulary"
        )

        food_deck = Deck(
            name="Food & Dining",
            description="Common food items and restaurant phrases"
        )

        db.add_all([basic_deck, numbers_deck, food_deck])
        db.flush()  # This will assign IDs to the decks

        # Basic Mandarin flashcards
        basic_flashcards = [
            Flashcard(
                word="你好",
                pinyin="nǐ hǎo",
                translation="hello",
                example_sentence="你好，早上好！",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="谢谢",
                pinyin="xiè xiè",
                translation="thank you",
                example_sentence="谢谢你的帮助。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="再见",
                pinyin="zài jiàn",
                translation="goodbye",
                example_sentence="明天见，再见！",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="对不起",
                pinyin="duì bù qǐ",
                translation="sorry",
                example_sentence="对不起，我迟到了。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="没关系",
                pinyin="méi guān xi",
                translation="it's okay/no problem",
                example_sentence="没关系，不用担心。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="我",
                pinyin="wǒ",
                translation="I/me",
                example_sentence="我是学生。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="你",
                pinyin="nǐ",
                translation="you",
                example_sentence="你是老师吗？",
                deck_id=basic_deck.id
            ),
        ]

        # Numbers & Time flashcards
        number_flashcards = [
            Flashcard(
                word="一",
                pinyin="yī",
                translation="one",
                example_sentence="我要一个苹果。",
                deck_id=numbers_deck.id
            ),
            Flashcard(
                word="二",
                pinyin="èr",
                translation="two",
                example_sentence="我有两个姐姐。",
                deck_id=numbers_deck.id
            ),
            Flashcard(
                word="三",
                pinyin="sān",
                translation="three",
                example_sentence="三点钟。",
                deck_id=numbers_deck.id
            ),
            Flashcard(
                word="星期一",
                pinyin="xīng qī yī",
                translation="Monday",
                example_sentence="星期一我去上学。",
                deck_id=numbers_deck.id
            ),
            Flashcard(
                word="分钟",
                pinyin="fēn zhōng",
                translation="minute",
                example_sentence="等五分钟。",
                deck_id=numbers_deck.id
            ),
            Flashcard(
                word="小时",
                pinyin="xiǎo shí",
                translation="hour",
                example_sentence="我学习了三个小时。",
                deck_id=numbers_deck.id
            ),
        ]

        # Food & Dining flashcards
        food_flashcards = [
            Flashcard(
                word="米饭",
                pinyin="mǐ fàn",
                translation="rice",
                example_sentence="我想吃米饭。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="水",
                pinyin="shuǐ",
                translation="water",
                example_sentence="请给我一杯水。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="茶",
                pinyin="chá",
                translation="tea",
                example_sentence="中国茶很有名。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="筷子",
                pinyin="kuài zi",
                translation="chopsticks",
                example_sentence="请给我一双筷子。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="餐厅",
                pinyin="cān tīng",
                translation="restaurant",
                example_sentence="这个餐厅很好吃。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="菜单",
                pinyin="cài dān",
                translation="menu",
                example_sentence="服务员，请给我菜单。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="饿",
                pinyin="è",
                translation="hungry",
                example_sentence="我很饿。",
                deck_id=food_deck.id
            ),
        ]

        # Add all flashcards to the database
        db.add_all(basic_flashcards)
        db.add_all(number_flashcards)
        db.add_all(food_flashcards)

        db.commit()
        print("Database populated successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error populating database: {str(e)}")
    finally:
        db.close()


if __name__ == "__main__":
    populate_database()
