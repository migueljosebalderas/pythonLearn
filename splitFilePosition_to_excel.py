"""
Autor: Miguel Jose Balderas
Leer archivo de texto, separado por posicion y pasar los datos a un archivo de excel
"""

from openpyxl import Workbook

wb_result = Workbook()
ws_result = wb_result.create_sheet()
ws_result.title = "Los datos"

archivo = open("data.txt","r")

for linea in archivo:
    #print(linea)
    Nombre=linea[0:7]
    App=linea[8:19]
    Edad=linea[20:22]
    print("Nombre es:", Nombre)
    print("Apellido es:", App)
    print("Edad es:", Edad)
    lista = [Nombre,App,Edad]
    tupla = tuple(lista)
    print(tupla)
    print("")
    ws_result.append(tupla)

wb_result.save("datos.xlsx")
archivo.close()