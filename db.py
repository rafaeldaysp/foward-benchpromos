import sqlite3

class Database():
    def __init__(self, dbName: str) -> None:
      self.conn = sqlite3.connect(dbName)
      self.cursor = self.conn.cursor()
    
    def createTable(self, tableName: str, **kargs) -> None:
      sqlQuery = f"CREATE TABLE IF NOT EXISTS {tableName} ("
      columns = []
      for column, columnType in kargs.items():
          columns.append(f"{column} {columnType}")
      sqlQuery += ", ".join(columns)
      sqlQuery += ");"

      self.conn.execute(sqlQuery)
      self.conn.commit()
   
    def fetchTable(self, tableName: str, *args) -> list:
      desiredColumns = '*'
      if args:
        desiredColumns = ", ".join(args)
      
      return self.conn.execute(f"SELECT {desiredColumns} from {tableName}").fetchall()

    def conditionalFetchTable(self, tableName, *args, **kwargs) -> list:
      desiredColumns = '*'
      if args:
        desiredColumns = ", ".join(args)
      key, value = list(kwargs.items())[0]
      sqlQuery = f"SELECT {desiredColumns} from {tableName} WHERE {key}=?"
      sqlParams = value
      
      return self.conn.execute(sqlQuery, (sqlParams,)).fetchall()
    
    def insertIntoTable(self, tableName, **kwargs) -> None:
      placeholders = ", ".join(["?" for _ in kwargs])
      columns = ", ".join(kwargs.keys())
      values = tuple(kwargs.values())
      sqlQuery = f"INSERT INTO {tableName} ({columns}) VALUES ({placeholders});"
      self.conn.execute(sqlQuery, values)
      self.conn.commit()
      
    def updateTable(self, tableName: str, columns: dict, **kwargs):
      set_values = ", ".join([f"{column} = ?" for column in columns.keys()])
      keyCondition, valueCondition = list(kwargs.items())[0]
      sqlQuery = f"UPDATE {tableName} SET {set_values} WHERE {keyCondition}=?"
      sqlParams = list(columns.values())
      sqlParams.append(valueCondition)
      self.conn.execute(sqlQuery, tuple(sqlParams))
      self.conn.commit()
    
    def closeConnection(self) -> None:
      self.conn.close()