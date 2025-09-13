# Using Flask to get information from the front end and pass it to the test layer, then the
# service layer, then the data access layer.
from flask import Flask, request, jsonify
from entities.reader import Reader
from data_access_layer.reader_data_access import ReaderDataAccess
import mysql.connector

# CONNECTOR OBJECT FOR POST REQUESTS


# READER LOGIN: receive user email and password to login. Data passed to the test layer.
# BOOK CREATION: add book details to create a book and add it to the user's book list.
# LIST BOOKS: show reader's book list.
# READER LOGOUT: log out the reader.

# Creating an object of the Flask class. "__name__" is passed into the instantiated object to tell
# the Flask class to request the necessary files and templates.
app = Flask(__name__)

# REGISTER/CREATE READER
# Use the "route" decorator and specify the add-on portion of the website url in parentheses.
# When the user fills out the register form the form action will specify the /register route and
# that will activate the function right below this decorator called "create_reader()".
@app.post("/register")
def create_reader():
    try:
        # The information passed through the HTTP request with JavaScript at the front end is requested
        # by this /register route (form action) and parsed into a JSON dictionary format, needed in the
        # same format as the reader entity dictionary method. The JSON dictionary is saved in the
        # variable "new_reader_data".
        reader_data = request.get_json()
        # The JSON dictionary of information received from the front end is then used to create a
        # new reader object with the imported Reader entity. The readerId data is a temporary value
        # because the real id is automatically created in the database as a SERIAL value. However,
        # we still need that readerId parameter to correctly instantiate the reader object.
        new_reader_object = Reader(reader_data["readerId"], reader_data["firstName"],
                                   reader_data["readerEmail"], reader_data["readerPassword"])
        # Send the newly instantiated reader object to the data access layer's register_reader()
        # method. It will move onto the database, be added to the proper DB table and the method's
        # returned reader object will be stored in "reader_to_database".
        reader_to_database = ReaderDataAccess.register_reader(new_reader_object)
        # Use the entity's dictionary method to recollect the reader object's information in a
        # dictionary.
        reader_to_frontend = reader_to_database.reader_dictionary()
        # Turn the reader object's Python dictionary into a JSON dictionary that will be sent back
        # to the front end, along with the 201 response code.
        return "WORKED PROPERLY - FROM MAIN.PY"
    except:
        return "DIDN'T WORK PROPERLY - FROM MAIN.PY"

@app.route("/test")
def make_routes():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()