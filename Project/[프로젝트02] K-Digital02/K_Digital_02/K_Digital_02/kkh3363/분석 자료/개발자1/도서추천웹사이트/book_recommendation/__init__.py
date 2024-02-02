from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    Bootstrap(app)

    from .routes import book_bp
    app.register_blueprint(book_bp)

    return app
