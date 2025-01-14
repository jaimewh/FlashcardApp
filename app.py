from flask import Flask, render_template
from src.routes.decks import decks_bp
from src.routes.review import review_bp
from src.database.db import engine, Base
import os

app = Flask(__name__,
    template_folder='src/templates',
    static_folder='src/static'
)

# Register blueprints
app.register_blueprint(decks_bp)
app.register_blueprint(review_bp)

# Set a secret key for session management
app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))

# Add home route
@app.route('/')
def index():
    return render_template('home.html')

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
