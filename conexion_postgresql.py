import psycopg2

def Abrir_baseDatos(self):
    # Conexión a la base de datos
    self.conn = psycopg2.connect(host="localhost", database="Boveda", user="postgres", password="j088058495r")

    # Creación de un cursor para realizar consultas a la base de datos
    self.cur = self.conn.cursor()
    print("BD abierta")
  
   
def Cerrar_baseDatos(self):
     # Cierre del cursor y la conexión a la base de datos
    self.cur.close()
    self.conn.close()
    print("BD Cerrada")
