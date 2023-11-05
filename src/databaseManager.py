from flask import jsonify
from .config import DB_config
import json
from model.dom import Books, db
from sqlalchemy import func

class DatabaseManager:
    def __init__(self):
        # Constructor for the DatabaseManager class
        # You can perform database initializations here
        pass

    def __finally__(self):
        # Cleanup method; if you need to close connections or cursors, you can implement it here
        pass

    def addBook(self, data: dict):
        # Method for adding a new book to the Books table
        print('[DatabaseManager.py] [addBook] adding a new book to the Books table')

        # Extract values from the input data dictionary
        isbn = data.get('ISBN')
        author = data.get('author')
        title = data.get('title')
        summary = data.get('summary')
        cover_url = data.get('cover_url')

        try:
            # Execute the query to add a new book
            newBook = Books(isbn=isbn, author=author, title=title, summary=summary, cover_url=cover_url)
            db.session.add(newBook)
            # Commit the changes to the database
            db.session.commit()
            print('[DatabaseManager.py] [addBook] book Successfully added to the table')
            # Call the cleanup method if needed
            # self.__finally__()
            return 'success'

        except Exception as e:
            # Call the cleanup method if needed
            # self.__finally__()
            return 'ERROR!! ' + str(e)

    def getBook(self, isbn):
        # Method for retrieving book details by ISBN
        print('[DatabaseManager.py] [getBook] retrieving book details of ISBN ' + isbn)

        try:
            # Query for retrieving book records based on ISBN
            response = Books.query.filter_by(isbn=isbn).first()
            if response:
                return response.to_json()
            else:
                print('[DatabaseManager.py] [getBook] No book found for the ISBN ' + isbn)
                return ''
        except Exception as e:
            return 'ERROR!! ' + str(e)

    def getAllBooks(self):
        # Method for retrieving all books from the "books" table
        print('[DatabaseManager.py] [__getAllBooks__] retrieving all books from books table')

        try:
            response = Books.query.all()
            print('[DatabaseManager.py] [__getAllBooks__] Successfully retrieved data')
            if response:
                # Convert the response to JSON format
                response = [book.to_json() for book in response]
                return json.dumps(response)
            else:
                return ''

        except Exception as e:
            return 'ERROR!! ' + str(e)
