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