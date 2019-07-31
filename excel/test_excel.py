from unittest import TestCase
from excel import Excel

class ExcelTest(TestCase):

    def test_readCount(self):
        """Registros leidos del excel"""
        xl = Excel()
        data = xl.read_file("samplexl.xlsx","datosm")
        
        self.assertEqual(len(data),3)

    def test_read_data(self):
        """La información es correcta"""
        xl = Excel()
        data = xl.read_file("samplexl.xlsx","datosm")

        data_expected = [("Nombre","App","Apm"), ("Miguel","Bal","Gar"), ("Eira","Garcia","Mata")]

        self.assertEqual(data,data_expected)

    def test_write_file(self):
        """Archivo de excel generado de manera correcta"""
        xl = Excel()
        data = [ ["No Cliente","Nombre"],["1948393849383","MBalderas"],["853939383938293","Santiago Bald"] ]
        xl.write_file("prueba1","result-val",data)

        self.assertTrue(True)

    def test_read_header(self):
        """Lectura de encabezados de archivo excel"""
        xl = Excel()
        data = xl.read_file("samplexl.xlsx","datosm")
        headers=("Nombre","App","Apm")

        self.assertEqual(xl.get_headers(), headers)
