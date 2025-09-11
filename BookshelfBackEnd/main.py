# Using Flask to get information from the front end and pass it to the test layer, then the
# service layer, then the data access layer.
from flask import Flask, request, jsonify
from entities.reader import Reader

# READER LOGIN: receive user email and password to login. Data passed to the test layer.
# BOOK CREATION: add book details to create a book and add it to the user's book list.
# LIST BOOKS: show reader's book list.
# READER LOGOUT: log out the reader.

# Creating an object of the Flask class. "__name__" is passed into the instantiated object to tell
# the Flask class to request the necessary files and templates.
app = Flask(__name__)

# REGISTER/CREATE READER
# Use the "route" decorator and specify the add-on portion of the main website url in parentheses.
# When the user goes to www.main-url.com/reader they will activate the function right below this
# decorator called "create_reader()".
@app.route("/reader")
def create_reader():
    try:
        new_reader_data = request.get_json()
        new_reader_object = Reader(new_reader_data["readerId"], new_reader_data["firstName"],
                                   new_reader_data["email"], new_reader_data["password"])
        # reader_json_to_service_layer =
    except:
        pass

@app.route("/test")
def make_routes():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()