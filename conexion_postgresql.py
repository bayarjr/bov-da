"""
import psycopg2

try:
    connection=psycopg2.connect(
        database='Boveda',
        host='localhost',
        user= 'postgres',
        password='Acciowombat5268',
        port='5432'
        )
    
    cur = connection.cursor()
    cur.execute('''CREATE TABLE contrasenas
       (ID SERIAL PRIMARY KEY,
       SITIO TEXT NOT NULL,
       USUARIO TEXT NOT NULL,
       CONTRASENA TEXT NOT NULL);''')
    connection.commit()

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
    user="posgresql",
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