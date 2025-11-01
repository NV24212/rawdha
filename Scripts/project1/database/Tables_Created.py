import psycopg2

def createtables():
   conn = psycopg2.connect(database="database_free", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("CREATE TABLE register(id SERIAL PRIMARY KEY, class VARCHAR(30), name VARCHAR(255), cpr VARCHAR(30), address VARCHAR(255), contact1 VARCHAR(30), contact2 VARCHAR(30), feez INT ,date DATE , add_from  VARCHAR(50));")
   cur.execute("CREATE TABLE come_abs_late(id SERIAL PRIMARY KEY, class VARCHAR(30), name VARCHAR(255), status VARCHAR(30), date DATE, add_from  VARCHAR(50));")
   cur.execute("CREATE TABLE bills(id SERIAL PRIMARY KEY, invoice_type VARCHAR(30), invoice_no VARCHAR(30), description VARCHAR(255), amount INT, date DATE, add_from  VARCHAR(50));")
   cur.execute("CREATE TABLE income(id SERIAL PRIMARY KEY, name  VARCHAR(255), cpr  VARCHAR(255), description VARCHAR(255), amount INT, date DATE, add_from  VARCHAR(50));")
   cur.execute("CREATE TABLE salaries(id SERIAL PRIMARY KEY, name  VARCHAR(255), cpr  VARCHAR(255), salary INT, date DATE, add_from  VARCHAR(50));")        

   print("Tables Created")
   conn.commit()
   cur.close() 
   conn.close()

createtables()

