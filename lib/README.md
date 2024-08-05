
## Installation

1. **Clone the repository:**

    
    git clone https://github.com/vundi4773/py3-cli-projects.git
    cd lib_cli
    

2. **Install dependencies using Pipenv:**

    pipenv install
    

3. **Activate the virtual environment:**

    
    pipenv shell
    

4. **Set up the database:**

    sh
    cd lib/db
    alembic init migrations
    

5. **Configure Alembic:**

    Edit `lib/db/migrations/alembic.ini` to set the `sqlalchemy.url` to point to your database (e.g., `sqlite:///../../library.db`).

6. **Run the initial migration:**

    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head

7. **Generate test data:**

    pipenv run python seed.py

## Usage

The CLI provides several commands to manage authors, books, and categories.

1. **List available commands:**

    ```sh
    python lib/cli.py --help
    ```

2. **Add a new author:**

    ```sh
    python lib/cli.py add-author "Author Name"
    ```

3. **Add a new book:**

    ```sh
    python lib/cli.py add-book "Book Title" 2024 1 1 2
    ```

4. **Add a new category:**

    ```sh
    python lib/cli.py add-category "Category Name"
    ```

5. **List all authors:**

    ```sh
    python lib/cli.py list-authors
    ```

6. **List all books:**

    ```sh
    python lib/cli.py list-books
    ```

7. **List all categories:**

    ```sh
    python lib/cli.py list-categories
    ```

## Project Details

- **CLI Application:** Created using Click to provide commands for managing library data.
- **Database:** Managed with SQLAlchemy ORM and Alembic for migrations.
- **Virtual Environment:** Maintained using Pipenv for dependency management and virtual environment.
- **Test Data:** Generated using the Faker library.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

