import json
import requests
from flask import request
from flask_restful import Resource
from .initialiseManager import databaseManager

class GetBooks(Resource):
    """
        Handle HTTP GET requests to retrieve all books.

        This method processes the incoming request to retrieve all books from the database.
        It calls the `databaseManager` to fetch all books and returns them as a JSON response.

        Returns:
            - JSON response with all books, status code 200 (OK).
            - 'ERROR' in case of any error.
    """

    def get(self):
        print('[app.py] [/GetBooks] got request')
        try:
            # Call the databaseManager to fetch all books
            print('[app.py] [/GetBooks] calling databaseManager GetBooks')
            res = databaseManager.getAllBooks()
            if len(res)!=0:
                # Return the retrieved books as JSON response with a status code of 200 (OK)
                return json.loads(res), 200
            else:
                # Return an empty list as a JSON response with a status code of 200 (OK)
                return [], 200
        except Exception as e:
            # If an exception is raised, print an error message
            print('ERRORR!! [app.py] [GetBooks]' + str(e))
            # Return an error response
            return 'ERROR'
