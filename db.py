import os
from tinydb import TinyDB, Query

DB_PATH = f"{os.getcwd()}/db/index"

class DB:
    def __init__(self):
        self.db = TinyDB(DB_PATH)
    
    def insert(self, tableName, data):
        table = self.db.table(tableName)

        table.insert(data)

    def get(self, tableName, field, data):
        table = self.db.table(tableName)
        query = Query()

        return table.get(query[field] == data)

    def get_all(self, tableName):
        table = self.db.table(tableName)

        return table.all()
    
    def update(self, tableName,field, fieldData, data):
        table = self.db.table(tableName)
        query = Query()

        table.update(data, query[field] == fieldData)
