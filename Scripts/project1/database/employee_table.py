import psycopg2

def create_employees():
   conn = psycopg2.connect(database="database_free", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("CREATE TABLE employees(id SERIAL PRIMARY KEY, name VARCHAR(255), cpr VARCHAR(30), job VARCHAR(255), address VARCHAR(255), contact VARCHAR(30), salary INT,joindate DATE, add_from  VARCHAR(50));")
   print("Employee Table Created")
   conn.commit()
   cur.close() 
   conn.close()

create_employees()

