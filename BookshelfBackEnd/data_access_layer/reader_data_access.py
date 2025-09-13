from entities.reader import Reader
from abstract_layer.abstract_reader import ReaderBlueprint
from db_layer.database_connection import run_app

class ReaderDataAccess(ReaderBlueprint):

    def register_reader(self, reader: Reader) -> Reader:
        sql_command = 'insert into "BookshelfDB".reader values(default, %s, %s, %s) returning readerID'
        cursor = run_app().cursor()
        cursor.execute(sql_command, (reader.first_name, reader.email, reader.password))
        db_reader_id = cursor.fetchone()[0]
        reader.reader_id = db_reader_id
        run_app().commit()
        return reader

    def reader_login(self, username: str, password: str):
        pass

    def change_reader_details(self, reader_id: int):
        pass

    def reader_logout(self, reader_id: int):
        pass