import json
from flask import request, jsonify
from flask_restful import Resource
from .initialiseManager import databaseManager
from .isValidISBN import ValidateISBN
import requests
from .config import OpenLibraryAPI

class FetchBook(Resource):
    def get(self, isbn):
        """
        Handle HTTP GET requests to retrieve book information by ISBN.

        This method processes the incoming request to retrieve book details based on its ISBN.
        It first checks if the ISBN is valid, and if the book is found in the local database.
        If not found locally, it queries an external Open Library API to fetch book information.

        Returns:
            - JSON response with book information, status code 200 (OK), if the book is found.
            - 'Not found' with status code 204 (No Content) if the book is not found.
            - 'Error!! Invalid ISBN' with status code 400 (Bad Request) if the provided ISBN is invalid.
            - 'ERROR' in case of any other error.
        """

        print('[app.py] [/FetchBook] got request')
        try:
            print('[app.py] [/FetchBook] Retrieved ISBN number is ' + isbn)
            print('[app.py] [/FetchBook] calling databaseManager FetchBook')
            
            # Validate the retrieved ISBN before processing it
            if ValidateISBN(isbn):
                # Call databaseManager to get book details from the local database
                res = databaseManager.getBook(isbn=isbn)

                # Checking if the book is found in the local database
                if res != '':
                    #If book is found in local database return teh book information is json format
                    return res
                else:
                    # If the book is not found in the local database, query the external OpenLibraryAPI
                    external_library = OpenLibraryAPI(isbn=isbn)
                    res = requests.get(external_library.url, external_library.params)
                    response_data = json.loads(res.content)

                    if len(response_data) == 0:
                        # If no book information is found, return 'Not found' with a status code of 204 (No Content)
                        return 'Not found', 204
                    else:
                        # Extract the author, title, summary, and cover URL from the response
                        book_info = response_data.get(f"ISBN:{isbn}")
                        details = book_info.get("details", {})
                        author = details.get("authors", [{}])[0].get("name", "Author not found")
                        title = details.get("title", "Title not found")
                        summary = details.get("subtitle", "Summary not found")
                        cover_url = book_info.get("thumbnail_url", "Cover URL not found")
                        #Creating Json response with extracted Values
                        json_res = {'ISBN': isbn, 'author': author, 'title': title, 'summary': summary, 'cover_url': cover_url}
                        return json_res, 200
            else:
                # If the ISBN is invalid, print an error message
                print('[app.py] [/FetchBook] ERROR!! Provided ISBN is invalid')
                # Return an error response with a status code of 400 (Bad Request)
                return 'Error!! Invalid ISBN', 400
        except Exception as e:
            # If an exception is raised, print an error message
            print('ERRORR!! [app.py] [FetchBook]' + str(e))
            # Return an error response
            return 'ERROR'
