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

        number_deck = Deck(
            name="Numbers",
            description="Number related vocabulary"
        )

        time_deck = Deck(
            name="Time",
            description="Time related vocabulary"
        )

        food_deck = Deck(
            name="Food & Dining",
            description="Common food items and restaurant phrases"
        )

        db.add_all([basic_deck, number_deck, time_deck, food_deck])
        db.flush()  # This will assign IDs to the decks

        # Basic Mandarin flashcards
        basic_flashcards = [
            Flashcard(
                word="谢谢",
                pinyin="xièxie",
                translation="thank you",
                example_sentence="谢谢你的帮助！",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="对不起",
                pinyin="duìbuqǐ",
                translation="sorry",
                example_sentence="对不起，我迟到了。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="请",
                pinyin="qǐng",
                translation="please",
                example_sentence="请问，洗手间在哪里？",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="再见",
                pinyin="zàijiàn",
                translation="goodbye",
                example_sentence="明天见，再见！",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="是",
                pinyin="shì",
                translation="to be",
                example_sentence="他是我的朋友。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="不是",
                pinyin="bú shì",
                translation="not to be",
                example_sentence="这不是我的书。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="有",
                pinyin="yǒu",
                translation="to have",
                example_sentence="我有三个苹果。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="没有",
                pinyin="méiyǒu",
                translation="do not have",
                example_sentence="我没有时间。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="好",
                pinyin="hǎo",
                translation="good",
                example_sentence="今天天气很好。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="不好",
                pinyin="bù hǎo",
                translation="not good",
                example_sentence="这顿饭不好吃。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="大",
                pinyin="dà",
                translation="big",
                example_sentence="那是一只很大的狗。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="小",
                pinyin="xiǎo",
                translation="small",
                example_sentence="这个房间太小了。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="家",
                pinyin="jiā",
                translation="home; family",
                example_sentence="我家住在伦敦。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="学校",
                pinyin="xuéxiào",
                translation="school",
                example_sentence="她的学校很大。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="吃",
                pinyin="chī",
                translation="to eat",
                example_sentence="我们一起吃午饭吧。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="喝",
                pinyin="hē",
                translation="to drink",
                example_sentence="我想喝一杯水。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="喜欢",
                pinyin="xǐhuan",
                translation="to like",
                example_sentence="我喜欢听音乐。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="朋友",
                pinyin="péngyou",
                translation="friend",
                example_sentence="这是我的好朋友。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="中国",
                pinyin="Zhōngguó",
                translation="China",
                example_sentence="我想去中国旅游。",
                deck_id=basic_deck.id
            ),
            Flashcard(
                word="英国",
                pinyin="Yīngguó",
                translation="United Kingdom",
                example_sentence="她是英国人。",
                deck_id=basic_deck.id
            ),
        ]

        # Numbers flashcards
        number_flashcards = [
            Flashcard(
                word="一",
                pinyin="yī",
                translation="one",
                example_sentence="我要一个苹果。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="二",
                pinyin="èr",
                translation="two",
                example_sentence="我有二十块钱。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="三",
                pinyin="sān",
                translation="three",
                example_sentence="他买了三本书。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="四",
                pinyin="sì",
                translation="four",
                example_sentence="这个房间有四个窗户。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="五",
                pinyin="wǔ",
                translation="five",
                example_sentence="我有五个朋友。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="六",
                pinyin="liù",
                translation="six",
                example_sentence="今天是六月六号。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="七",
                pinyin="qī",
                translation="seven",
                example_sentence="我每天早上七点起床。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="八",
                pinyin="bā",
                translation="eight",
                example_sentence="他们有八只猫。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="九",
                pinyin="jiǔ",
                translation="nine",
                example_sentence="九点钟我要去上班。",
                deck_id=number_deck.id
            ),
            Flashcard(
                word="十",
                pinyin="shí",
                translation="ten",
                example_sentence="我们十点在学校见。",
                deck_id=number_deck.id
            )
        ]

        # Time flashcards
        time_flashcards = [
            Flashcard(
                word="早上",
                pinyin="zǎoshang",
                translation="morning",
                example_sentence="早上好！今天吃了早餐吗？",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="中午",
                pinyin="zhōngwǔ",
                translation="noon",
                example_sentence="中午我们一起吃饭吧。",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="下午",
                pinyin="xiàwǔ",
                translation="afternoon",
                example_sentence="我下午三点有一个会议。",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="晚上",
                pinyin="wǎnshang",
                translation="evening",
                example_sentence="晚上我们去看电影，好吗？",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="现在",
                pinyin="xiànzài",
                translation="now",
                example_sentence="现在几点了？",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="几点",
                pinyin="jǐ diǎn",
                translation="what time",
                example_sentence="请问现在几点？",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="分钟",
                pinyin="fēnzhōng",
                translation="minute",
                example_sentence="等我五分钟。",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="小时",
                pinyin="xiǎoshí",
                translation="hour",
                example_sentence="我们学习了两个小时。",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="今天",
                pinyin="jīntiān",
                translation="today",
                example_sentence="今天是星期几？",
                deck_id=time_deck.id
            ),
            Flashcard(
                word="明天",
                pinyin="míngtiān",
                translation="tomorrow",
                example_sentence="明天我们去公园吧。",
                deck_id=time_deck.id
            )
        ]

        # Food & Dining flashcards
        food_flashcards = [
            Flashcard(
                word="筷子",
                pinyin="kuàizi",
                translation="chopsticks",
                example_sentence="请给我一双筷子。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="米饭",
                pinyin="mǐfàn",
                translation="rice",
                example_sentence="我每天都吃米饭。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="面条",
                pinyin="miàntiáo",
                translation="noodles",
                example_sentence="这碗面条很好吃。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="饺子",
                pinyin="jiǎozi",
                translation="dumpling",
                example_sentence="我喜欢吃猪肉饺子。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="汤",
                pinyin="tāng",
                translation="soup",
                example_sentence="这碗汤太热了。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="茶",
                pinyin="chá",
                translation="tea",
                example_sentence="我最喜欢喝绿茶。",
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
                word="苹果",
                pinyin="píngguǒ",
                translation="apple",
                example_sentence="你想吃苹果吗？",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="香蕉",
                pinyin="xiāngjiāo",
                translation="banana",
                example_sentence="这根香蕉很甜。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="鸡肉",
                pinyin="jīròu",
                translation="chicken",
                example_sentence="我想吃一盘鸡肉。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="牛肉",
                pinyin="niúròu",
                translation="beef",
                example_sentence="牛肉面是我的最爱。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="鱼",
                pinyin="yú",
                translation="fish",
                example_sentence="这道菜是清蒸鱼。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="蛋糕",
                pinyin="dàngāo",
                translation="cake",
                example_sentence="生日快乐！这是你的蛋糕。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="糖果",
                pinyin="tángguǒ",
                translation="candy",
                example_sentence="小孩子都喜欢吃糖果。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="冰淇淋",
                pinyin="bīngqílín",
                translation="ice cream",
                example_sentence="夏天吃冰淇淋最舒服了。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="蔬菜",
                pinyin="shūcài",
                translation="vegetable",
                example_sentence="多吃蔬菜对身体好。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="水果",
                pinyin="shuǐguǒ",
                translation="fruit",
                example_sentence="每天吃水果有益健康。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="早餐",
                pinyin="zǎocān",
                translation="breakfast",
                example_sentence="今天的早餐是面包和牛奶。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="午餐",
                pinyin="wǔcān",
                translation="lunch",
                example_sentence="午餐我们吃了炒饭。",
                deck_id=food_deck.id
            ),
            Flashcard(
                word="晚餐",
                pinyin="wǎncān",
                translation="dinner",
                example_sentence="晚餐时我们喝了红酒。",
                deck_id=food_deck.id
            )
        ]

        # Add all flashcards to the database
        db.add_all(basic_flashcards)
        db.add_all(number_flashcards)
        db.add_all(time_flashcards)
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
