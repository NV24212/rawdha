import psycopg2

def add_tables():
   conn = psycopg2.connect(database="database_free", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("CREATE TABLE come(id SERIAL PRIMARY KEY, class VARCHAR(30), name VARCHAR(255), status VARCHAR(30), date DATE, add_from  VARCHAR(50));")
   cur.execute("CREATE TABLE absent(id SERIAL PRIMARY KEY, class VARCHAR(30), name VARCHAR(255), status VARCHAR(30), date DATE, add_from  VARCHAR(50));")      
   cur.execute("CREATE TABLE late(id SERIAL PRIMARY KEY, class VARCHAR(30), name VARCHAR(255), status VARCHAR(30), date DATE, add_from  VARCHAR(50));")
   print("Add Created")
   conn.commit()
   cur.close() 
   conn.close()

add_tables()

