import sqlite3

class DataBase:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.curs = self.conn.cursor()

    def executeSQL(self,sql):
        """Ejecuta una sentencia ddl"""
        self.curs.execute(sql)
    
    def executeQuery_fetch(self,sql_query)
        """Ejecuta query regresa los resultados"""
        self.executeSQL(sql_query)
        data = self.curs.fetchall()
        return data
    
    def loadData(self,table, data)
        """Carga los datos en la tabla indicada"""
        cols_total = len(data[0])
        self.curs.executemany(self.get_sqlInsert(table,cols_total),data)
        self.conn.commit()

    def get_sqlInsert(table, cols_total):
        sql = "INSERT INTO " + table + " VALUES ("
        for n in range(0,cols_total):
            sql += "?,"
        sql = sql[0:len(sql)-1] + ")"
        return sql
