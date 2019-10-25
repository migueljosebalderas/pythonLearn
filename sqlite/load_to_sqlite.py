"""
Miguel Jose Balderas Diaz

Cargar archivo de datos a sqlite, datos separados por caracter indicado
parametros:
    file: archivo de datos
    delimiter: caracter delimitador, por defecto es coma
    databaseName: base donde se guardara la tabla
    tableName: nombre de la tabla 

"""

import sqlite3
import csv
import sys


def load_file(fileName, delim_char):
    print("archivo:", fileName)
    with open(fileName) as csv_file:
        data = csv.reader(csv_file,delimiter=delim_char)

        data_raw = []
            
        count = 0
        for row in data:
            if count == 0:
                execute_sql(prepare_create(row) )
            else:
                data_raw.append(tuple(row))
            count += 1
        
        load_data(data_raw)
            

def prepare_create(colums):
    sql = "Create table " + tableName + "("
    for col in colums:
        sql+= col + " text,"
    sql = sql[0:len(sql)-1] + ")"
    return sql

def execute_sql(sql):
    conn = sqlite3.connect(baseName)
    curs = conn.cursor()
    curs.execute(sql)
    conn.close()

def load_data(data):
    print("Total de regs:",len(data))
    conn = sqlite3.connect(baseName)
    curs = conn.cursor()
    cols_total = len(data[1])
    curs.executemany(get_sqlInsert(cols_total),data)
    conn.commit()
    conn.close() 

def get_sqlInsert(cols_total):
    sql = "INSERT INTO " + tableName + " VALUES ("
    for n in range(0,cols_total):
        sql += "?,"
    sql = sql[0:len(sql)-1] + ")"
    return sql
    


if __name__ == "__main__":
    try:
        fileName = sys.argv[1]
        delimiter = sys.argv[2]
        baseName = sys.argv[3]
        tableName = sys.argv[4]
    except:
        print("Faltan parametros")

    load_file(fileName)
    print("archivo cargado correctamente")

