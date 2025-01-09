from flask import Flask
from src.routes.decks import decks_bp
from src.database.db import engine, Base

app = Flask(__name__)
app.register_blueprint(decks_bp)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)