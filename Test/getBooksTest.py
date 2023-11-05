import unittest
from flask import Flask
from flask_restful import Api
from src.getBooks import GetBooks
from src.saveBook import SaveBooks  # Replace 'your_module_name' with the actual module name
from wsgi import app  # Replace 'your_module_name' with the actual module name

class GetBooksResourceTest(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and add the GetBooks resource
        self.app = app({
            'TESTING': True,  # Set TESTING to True to enable testing mode
        })
        self.api = Api(self.app)
        self.api.add_resource(GetBooks, '/books')
        self.api.add_resource(SaveBooks,'/books')

        self.client = self.app.test_client()

    def test_get_all_books_success(self):
        # Create a test case for successful retrieval of books
        with self.app.app_context():
            # Implement a mock getAllBooks method for the databaseManager
            def mock_get_all_books():
                self.client.post('/books', data={'isbn': '9780373033577'})
                self.client.post('/books', data={'isbn': '0553381687'})
                return '[{"title": "Book 1"}, {"title": "Book 2"}]'

            # Replace the actual databaseManager method with the mock method
            GetBooks.databaseManager.getAllBooks = mock_get_all_books

            # Send a GET request to the GetBooks endpoint
            response = self.client.get('/books')

            # Assert that the response status code is 200
            self.assertEqual(response.status_code, 200)

            # Assert that the response data matches the expected JSON data
            self.assertEqual(response.get_json(), [{"title": "Book 1"}, {"title": "Book 2"}])

    def test_get_all_books_empty(self):
        # Create a test case for an empty list of books
        with self.app.app_context():
            # Implement a mock getAllBooks method for the databaseManager
            def mock_get_all_books():
                return '[]'

            # Replace the actual databaseManager method with the mock method
            GetBooks.databaseManager.getAllBooks = mock_get_all_books

            # Send a GET request to the GetBooks endpoint
            response = self.client.get('/books')

            # Assert that the response status code is 200
            self.assertEqual(response.status_code, 200)

            # Assert that the response data is an empty list
            self.assertEqual(response.get_json(), [])

    def test_get_all_books_error(self):
        # Create a test case for an error in retrieving books
        with self.app.app_context():
            # Implement a mock getAllBooks method that raises an exception
            def mock_get_all_books():
                raise Exception("Database error")

            # Replace the actual databaseManager method with the mock method
            GetBooks.databaseManager.getAllBooks = mock_get_all_books

            # Send a GET request to the GetBooks endpoint
            response = self.client.get('/books')

            # Assert that the response status code is 200 (you may customize this based on your error handling)
            self.assertEqual(response.status_code, 200)

            # Assert that the response data is 'ERROR' (you may customize this based on your error handling)
            self.assertEqual(response.get_data(as_text=True), 'ERROR')

if __name__ == '__main__':
    unittest.main()
