import json
from flask import request, jsonify
from flask_restful import Resource
from .initialiseManager import databaseManager
from .isValidISBN import ValidateISBN
import requests
from .config import server_config

class SaveBooks(Resource):

    def post(self):
        """
        Handle HTTP POST requests to add a book to the database.

        This method processes the incoming request to add a book to the database based on its ISBN.
        It makes a GET request to retrieve book details by ISBN and then adds the book to the database.

        Returns:
            - 'success' with status code 201 (Created) if the book is successfully added to the database.
            - 'Error' with status code 400 (Bad Request) if there's an issue with the request.
            - 'ERROR' in case of any other error.
        
        """
        print('[app.py] [/SaveBooks] got request')
        try:
            # Retrieve the ISBN from the request's query parameters
            isbn = request.args['isbn']
            print('[app.py] [/SaveBooks] Retrieved ISBN number is ' + isbn)
            # Construct the URL to fetch book details using the ISBN
            print(f'http://{server_config.host}:{server_config.port}/isbn/{isbn}')
            # Make a GET request to the /isbn endpoint to fetch book details
            res = requests.get(url=f'http://{server_config.host}:{server_config.port}/isbn/{isbn}')
            if(res.status_code == 200):
                # If the request to fetch book details is successful (status code 200) add book to database table Books
                print('[app.py] [/SaveBooks] calling databaseManager adding book to the existing database table Books')
                # Add the book to the database by parsing the JSON response
                databaseManager.addBook(json.loads(res.content))
                # Return a success response with a status code of 201 (Created)
                return 'success', 201
            elif(res.status_code == 204):
                return 'Not Found', 204
            else:
                # If the request to fetch book details is not successful, return an error response with a status code of 400 (Bad Request)
                return 'Error', 400

        except Exception as e:
            # If an exception is raised, print an error message
            print('ERRORR!! [app.py] [SaveBooks]' + str(e))
            # Return an error response
            return 'ERROR'
