import psycopg2

def Abrir_baseDatos(self):
    # Conexión a la base de datos
    self.conn = psycopg2.connect(host="localhost", database="Boveda", user="postgres", password="j088058495r")

    # Cierre de conexión
    connection.close()
    print("Conexión exitosa")

    
except Exception as ex:
        print(ex)
        
"""

import psycopg2

# Conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="Boveda",
    user="postgres",
    password="Acciowombat5268"
)

# Creación de un cursor para realizar consultas a la base de datos
cur = conn.cursor()

# Ejecución de una consulta
cur.execute("SELECT * FROM contraseñas")

# Obtención de los resultados
resultados = cur.fetchall()

# Cierre del cursor y la conexión a la base de datos
cur.close()
conn.close()
""""
# Comprobación de la conexión
if conn.closed == 0:
    print("Conexión a la base de datos establecida")
else:
    print("No se pudo establecer la conexión a la base de datos")


"""
