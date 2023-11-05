from src.extensions import db

class Books(db.Model):
    
    #Defining database columns based on assumptions
    isbn = db.Column(db.String(13), primary_key=True) #General ISBN is 10-13 characters long including special characters
    author = db.Column(db.String(80), nullable=False) #General author name does not have any specific length
    title = db.Column(db.String(80), nullable=False) #General title can have any maximum characters length
    summary = db.Column(db.String(100)) #Generally summary is long
    cover_url = db.Column(db.String(50)) #cover_url length 

    def __init__(self,isbn,author,title,summary,cover_url):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.summary = summary
        self.cover_url = cover_url
       

    def to_json(self):
        return {
            'ISBN': self.isbn,
            'author': self.author,
            'title': self.title,
            'summary': self.summary,
            'cover_url': self.cover_url
        }

    def from_json(data):
        return Books(
            ISBN=data.get('isbn'),
            author=data.get('author'),
            title=data.get('title'),
            summary=data.get('summary'),
            cover_url=data.get('cover_url')
        )
