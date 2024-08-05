# lib/crud.py
from sqlalchemy.orm import Session
from models import Author, Book, Category

def create_author(db: Session, name: str) -> Author:
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def create_book(db: Session, title: str, year: int, author_id: int, category_ids: 'list[int]') -> Book:
    book = Book(title=title, year=year, author_id=author_id)
    db.add(book)
    db.commit()
    for category_id in category_ids:
        category = db.query(Category).get(category_id)
        book.categories.append(category)
    db.commit()
    db.refresh(book)
    return book

def create_category(db: Session, name: str) -> Category:
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_authors(db: Session) -> 'list[Author]':
    return db.query(Author).all()

def get_books(db: Session) -> 'list[Book]':
    return db.query(Book).all()

def get_categories(db: Session) -> 'list[Category]':
    return db.query(Category).all()
