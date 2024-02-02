from flask import Blueprint, render_template

book_bp = Blueprint('book', __name__)

@book_bp.route('/')
def index():
    return render_template('index.html', title='Book Recommendation')

@book_bp.route('/recommend')
def recommend():
    # Add logic for book recommendation here
    recommended_books = ["Book 1", "Book 2", "Book 3"]
    return render_template('recommend.html', title='Recommended Books', books=recommended_books)
