import os
#Server configuration
class server_config:
    host= '127.0.0.1'
    port = 80

basedir = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data'))
#Database configuration
DB_config = {'SQLALCHEMY_DATABASE_URI':'sqlite:///'+os.path.join(basedir,'books.db'),'SQLALCHEMY_TRACK_MODIFICATIONS':False}
print(DB_config)
#OpenLibrary API Configuration
class OpenLibraryAPI:
    def __init__(self, isbn):
        self.isbn = isbn
        self.url = 'https://openlibrary.org/api/books'
        self.params = {
            "bibkeys": f'ISBN:{self.isbn}',
            "format": 'json',
            "jscmd": "details"
        }



