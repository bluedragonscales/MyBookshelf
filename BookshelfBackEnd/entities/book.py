

class Book:
    def __init__(self, reader_id: int, book_id: int, title: str, author: str, copyright_year: str,
                 thoughts: str):
        self.reader_id = reader_id
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copyright_year = copyright_year
        self.thoughts = thoughts

    def book_dictionary(self):
        return {
            "readerId" : self.reader_id,
            "bookId" : self.book_id,
            "title" : self.title,
            "author" : self.author,
            "copyrightYear" : self.copyright_year,
            "thoughts" : self.thoughts
        }