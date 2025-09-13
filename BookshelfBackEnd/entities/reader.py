# The user entity will be called "reader". This blueprint will determine which details are stored
# and retrieved from the database to work with in the application. The constructor initializes the
# data needed to create the reader object. The reader_dictionary method is the JSON passed from
# database to front end to back end and reverse.

class Reader:
    def __init__(self, reader_id: int, first_name: str, email: str, password: str):
        self.reader_id = reader_id
        self.first_name = first_name
        self.email = email
        self.password = password

    def reader_dictionary(self):
        return {
            "readerId" : self.reader_id,
            "firstName" : self.first_name,
            "readerEmail" : self.email,
            "readerPassword" : self.password
        }
