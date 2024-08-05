# # lib/db/seed.py

from faker import Faker
from sqlalchemy.orm import Session
from lib.db.database import SessionLocal, init_db
from lib.db.crud import create_author, create_book, create_category

fake = Faker()

def generate_fake_data(db: Session, num_authors=10, num_categories=5, num_books=20):
    categories = []
    authors = []

    # Create categories
    for _ in range(num_categories):
        category_name = fake.word()
        category = create_category(db, category_name)
        categories.append(category)

    # Create authors
    for _ in range(num_authors):
        author_name = fake.name()
        author = create_author(db, author_name)
        authors.append(author)

    # Create books
    for _ in range(num_books):
        book_title = fake.sentence(nb_words=5)
        book_year = fake.year()
        author_id = fake.random_element(elements=authors).id
        category_ids = [fake.random_element(elements=categories).id for _ in range(fake.random_int(min=1, max=3))]
        create_book(db, book_title, int(book_year), author_id, category_ids)

def main():
    init_db()  # Initialize the database
    db = SessionLocal()

    try:
        generate_fake_data(db)
        print("Test data generated successfully.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
