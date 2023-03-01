import psycopg2

def In_baseDatos():
    # Conexión a la base de datos
    conn = psycopg2.connect(host="localhost", database="Boveda", user="postgres", password="j088058495r")

    # Creación de un cursor para realizar consultas a la base de datos
    cur = conn.cursor()
    print("Conexion ok")
    # Ejecución de una consulta
    cur.execute("SELECT * FROM contraseñas")

    # Obtención de los resultados
    resultados = cur.fetchall()

    # Cierre del cursor y la conexión a la base de datos
    cur.close()
    conn.close()
