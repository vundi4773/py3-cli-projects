# lib/cli.py
import click
from sqlalchemy.orm import Session
from lib.db.database import init_db, SessionLocal
from lib.db.crud import create_author, create_book, create_category, get_authors, get_books, get_categories

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    db: Session = SessionLocal()
    author = create_author(db, name)
    click.echo(f'Author added: {author.name}')

@click.command()
@click.argument('title')
@click.argument('year')
@click.argument('author_id')
@click.argument('category_ids', nargs=-1, type=int)
def add_book(title, year, author_id, category_ids):
    """Add a new book."""
    db: Session = SessionLocal()
    book = create_book(db, title, int(year), int(author_id), list(category_ids))
    click.echo(f'Book added: {book.title} ({book.year})')

@click.command()
@click.argument('name')
def add_category(name):
    """Add a new category."""
    db: Session = SessionLocal()
    category = create_category(db, name)
    click.echo(f'Category added: {category.name}')

@click.command()
def list_authors():
    """List all authors."""
    db: Session = SessionLocal()
    authors = get_authors(db)
    for author in authors:
        click.echo(f'{author.id}: {author.name}')

@click.command()
def list_books():
    """List all books."""
    db: Session = SessionLocal()
    books = get_books(db)
    for book in books:
        categories = ', '.join([category.name for category in book.categories])
        click.echo(f'{book.id}: {book.title} ({book.year}), Author: {book.author.name}, Categories: {categories}')

@click.command()
def list_categories():
    """List all categories."""
    db: Session = SessionLocal()
    categories = get_categories(db)
    for category in categories:
        click.echo(f'{category.id}: {category.name}')

cli.add_command(add_author)
cli.add_command(add_book)
cli.add_command(add_category)
cli.add_command(list_authors)
cli.add_command(list_books)
cli.add_command(list_categories)

if __name__ == '__main__':
    init_db()  # Initialize the database
    cli()
