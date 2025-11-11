from flask import render_template, request, current_app as app
from .database import get_db
from my_classes.user_manager import Users

@app.route("/")
def login():
   return render_template("login.html")


@app.route("/user_log", methods=['GET','POST'])
def user_log():

   user1 = Users("admin", "admin")
   user2 = Users("Abdul", "Abdul")
   user3 = Users("Abd", "Abd")
   user4 = Users("1234", "1234")

   if request.form['user'] and request.form['pass'] == user1.username and user1.password or request.form['user'] and request.form['pass'] == user2.username and user2.password or request.form['user'] and request.form['pass'] == user3.username and user3.password or request.form['user'] and request.form['pass'] == user4.username and user4.password:
     
      return render_template("index.html")
   else:
      return render_template("login.html")


@app.route("/admin_account_login", methods=['GET','POST'])
def admin_account_login():

      return render_template("admin_account_login.html")


@app.route("/ad_user_log", methods=['GET','POST'])
def ad_user_log():

   user5 = Users("1111", "1111")


   if request.form['ad_user'] and request.form['ad_pass'] == user5.username and user5.password:
     
      return render_template("the_accounts.html")
   else:
      return render_template("admin_account_login.html") 



@app.route("/administration")
def administration():
   return render_template("administration.html")

@app.route("/the_accounts")
def the_accounts():
   return render_template("the_accounts.html")

@app.route("/register")
def register():
   return render_template("register.html")

@app.route("/salaries")
def salaries():
   return render_template("salaries.html")

@app.route("/bills")
def bills():
   return render_template("bills.html")

@app.route("/come_abs_late")
def come_abs_late():
   return render_template("come_abs_late.html")

@app.route("/come")
def come():
   return render_template("come.html")

@app.route("/absent")
def absent():
   return render_template("absent.html")

@app.route("/late")
def late():
   return render_template("late.html")

@app.route("/income")
def income():
   return render_template("income.html")

@app.route("/reports")
def reports():
   return render_template("reports.html")

@app.route("/employees")
def employees():
   return render_template("employees.html")

@app.route("/search")
def search():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT name FROM register WHERE name <> 'test_only';")
      names = cur.fetchall()
   return render_template("search.html", names=names) 
    

@app.route("/student_information")
def student_information():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE name <> 'test_only';")
      rows = cur.fetchall()
   return render_template("student_information.html", rows = rows)

@app.route("/a_class")
def a_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'A%' ")
      rows = cur.fetchall()
   return render_template("a_class.html", rows = rows)

@app.route("/b_class")
def b_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'B%' ")
      rows = cur.fetchall()
   return render_template("b_class.html", rows = rows)

@app.route("/c_class")
def c_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'C%' ")
      rows = cur.fetchall()
   return render_template("c_class.html", rows = rows)

@app.route("/d_class")
def d_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'D%' ")
      rows = cur.fetchall()
   return render_template("d_class.html", rows = rows)

@app.route("/ee_class")
def ee_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'E%' ")
      rows = cur.fetchall()
   return render_template("ee_class.html", rows = rows)



@app.route("/f_class")
def f_class():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE class LIKE 'F%' ")
      rows = cur.fetchall()
   return render_template("f_class.html", rows = rows)


@app.route("/register_view")
def register_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("select * from register order by id desc limit 1; ")
      rows = cur.fetchall()
   return render_template("register_view.html", rows = rows)

@app.route("/income_view")
def income_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("select * from income order by id desc limit 1; ")
      rows = cur.fetchall()
   return render_template("income_view.html", rows = rows)

@app.route("/salaries_view")
def salaries_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("select * from salaries order by id desc limit 1; ")
      rows = cur.fetchall()
   return render_template("salaries_view.html", rows = rows)

@app.route("/employees_view")
def employees_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("select * from employees order by id desc limit 1; ")
      rows = cur.fetchall()
   return render_template("employees_view.html", rows = rows)

    


@app.route("/report1_open")
def report1_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM register WHERE name <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report1.html", rows = rows)

@app.route("/report2_open")
def report2_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute('SELECT * FROM come_abs_late;')
      rows = cur.fetchall()
   return render_template("report2.html", rows = rows)

@app.route("/report3_open")
def report3_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM bills WHERE invoice_type <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report3.html", rows = rows)

@app.route("/report4_open")
def report4_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM income WHERE name <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report4.html", rows = rows)

@app.route("/report5_open")
def report5_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM salaries WHERE name <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report5.html", rows = rows)

@app.route("/report6_open")
def report6_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM salaries WHERE name <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report6.html")

@app.route("/report7_open")
def report7_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM salaries WHERE name <> 'test_only' ;")
      rows = cur.fetchall()
   return render_template("report7.html")

@app.route("/report8_open")
def report8_open():
   with get_db().cursor() as cur:
      # Bills_Montly
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-1-1' AND '2025-1-31';")
      month1 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-2-1' AND '2025-2-28';")
      month2 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-3-1' AND '2025-3-31';")
      month3 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-4-1' AND '2025-4-30';")
      month4 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-5-1' AND '2025-5-31';")
      month5 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-6-1' AND '2025-6-30';")
      month6 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-7-1' AND '2025-7-31';")
      month7 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-8-1' AND '2025-8-31';")
      month8 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-9-1' AND '2025-9-30';")
      month9 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-10-1' AND '2025-10-31';")
      month10 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-11-1' AND '2025-11-30';")
      month11 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM bills WHERE date BETWEEN '2025-12-1' AND '2025-12-31';")
      month12 = cur.fetchone()[0]

      # Salaries_Montly
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-1-1' AND '2025-1-31';")
      smonth1 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-2-1' AND '2025-2-28';")
      smonth2 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-3-1' AND '2025-3-31';")
      smonth3 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-4-1' AND '2025-4-30';")
      smonth4 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-5-1' AND '2025-5-31';")
      smonth5 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-6-1' AND '2025-6-30';")
      smonth6 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-7-1' AND '2025-7-31';")
      smonth7 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-8-1' AND '2025-8-31';")
      smonth8 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-9-1' AND '2025-9-30';")
      smonth9 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-10-1' AND '2025-10-31';")
      smonth10 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-11-1' AND '2025-11-30';")
      smonth11 = cur.fetchone()[0]
      cur.execute("SELECT SUM(salary) FROM salaries WHERE date BETWEEN '2025-12-1' AND '2025-12-31';")
      smonth12 = cur.fetchone()[0]

      # Register_Montly
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-1-1' AND '2025-1-31';")
      rmonth1 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-2-1' AND '2025-2-28';")
      rmonth2 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-3-1' AND '2025-3-31';")
      rmonth3 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-4-1' AND '2025-4-30';")
      rmonth4 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-5-1' AND '2025-5-31';")
      rmonth5 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-6-1' AND '2025-6-30';")
      rmonth6 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-7-1' AND '2025-7-31';")
      rmonth7 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-8-1' AND '2025-8-31';")
      rmonth8 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-9-1' AND '2025-9-30';")
      rmonth9 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-10-1' AND '2025-10-31';")
      rmonth10 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-11-1' AND '2025-11-30';")
      rmonth11 = cur.fetchone()[0]
      cur.execute("SELECT SUM(feez) FROM register WHERE date BETWEEN '2025-12-1' AND '2025-12-31';")
      rmonth12 = cur.fetchone()[0]

      # income_Montly
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-1-1' AND '2025-1-31';")
      imonth1 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-2-1' AND '2025-2-28';")
      imonth2 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-3-1' AND '2025-3-31';")
      imonth3 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-4-1' AND '2025-4-30';")
      imonth4 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-5-1' AND '2025-5-31';")
      imonth5 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-6-1' AND '2025-6-30';")
      imonth6 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-7-1' AND '2025-7-31';")
      imonth7 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-8-1' AND '2025-8-31';")
      imonth8 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-9-1' AND '2025-9-30';")
      imonth9 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-10-1' AND '2025-10-31';")
      imonth10 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-11-1' AND '2025-11-30';")
      imonth11 = cur.fetchone()[0]
      cur.execute("SELECT SUM(amount) FROM income WHERE date BETWEEN '2025-12-1' AND '2025-12-31';")
      imonth12 = cur.fetchone()[0]

   return render_template("report8.html", month1=month1,month2=month2,month3=month3,month4=month4,
   month5=month5,month6=month6,month7=month7,month8=month8,
   month9=month9,month10=month10,month11=month11,month12=month12,
   smonth1=smonth1,smonth2=smonth2,smonth3=smonth3,smonth4=smonth4,
   smonth5=smonth5,smonth6=smonth6,smonth7=smonth7,smonth8=smonth8,
   smonth9=smonth9,smonth10=smonth10,smonth11=smonth11,smonth12=smonth12,
   rmonth1=rmonth1,rmonth2=rmonth2,rmonth3=rmonth3,rmonth4=rmonth4,
   rmonth5=rmonth5,rmonth6=rmonth6,rmonth7=rmonth7,rmonth8=rmonth8,
   rmonth9=rmonth9,rmonth10=rmonth10,rmonth11=rmonth11,rmonth12=rmonth12,
   imonth1=imonth1,imonth2=imonth2,imonth3=imonth3,imonth4=imonth4,
   imonth5=imonth5,imonth6=imonth6,imonth7=imonth7,imonth8=imonth8,
   imonth9=imonth9,imonth10=imonth10,imonth11=imonth11,imonth12=imonth12
   )

@app.route("/report9_open")
def report9_open():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute('SELECT SUM(amount) FROM income;')
      amount_sum = cur.fetchone()[0]

      cur.execute('SELECT SUM(feez) FROM register;')
      feez_sum = cur.fetchone()[0]

      cur.execute('SELECT SUM(amount) FROM bills;')
      bills_sum = cur.fetchone()[0]

      cur.execute('SELECT SUM(salary) FROM salaries;')
      salary_sum = cur.fetchone()[0]
   return render_template("report9.html", amount_sum = amount_sum,feez_sum=feez_sum , bills_sum = bills_sum, salary_sum = salary_sum)


@app.route("/late_view")
def late_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM late;")
      rows = cur.fetchall()
   return render_template("late_view.html", rows = rows)

@app.route("/come_view")
def come_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM come;")
      rows = cur.fetchall()
   return render_template("come_view.html", rows = rows)

@app.route("/absent_view")
def absent_view():
   conn = get_db()
   with conn.cursor() as cur:
      cur.execute("SELECT * FROM absent;")
      rows = cur.fetchall()
   return render_template("absent_view.html", rows = rows)


@app.route('/add_register',methods = ['POST'])
def add_register():
   conn = get_db()
   with conn.cursor() as cur:
      classx = request.form['class']
      namex = request.form['name']
      cprx = request.form['cpr']
      addressx = request.form['address']
      contact1x = request.form['contact1']
      contact2x = request.form['contact2']
      feezx = request.form['feez']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO register(class,name,cpr,address,contact1,contact2, feez, date, add_from)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(classx,namex,cprx,addressx,contact1x,contact2x,feezx,datex,add_fromx))
   conn.commit()
   return render_template("register.html")


@app.route('/add_come_abs_late',methods = ['POST'])
def add_come_abs_late():
   conn = get_db()
   with conn.cursor() as cur:
      classx = request.form['class']
      namex = request.form['name']
      statusx = request.form['status']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO come_abs_late(class,name,status,date,add_from)VALUES(%s,%s,%s,%s,%s)",(classx,namex,statusx,datex,add_fromx))
   conn.commit()
   return render_template("come_abs_late.html")


@app.route('/add_come',methods = ['POST'])
def add_come():
   conn = get_db()
   with conn.cursor() as cur:
      classx = request.form['class']
      namex = request.form['name']
      statusx = request.form['status']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO come(class,name,status,date,add_from)VALUES(%s,%s,%s,%s,%s)",(classx,namex,statusx,datex,add_fromx))
   conn.commit()
   return render_template("come.html")

@app.route('/add_absent',methods = ['POST'])
def add_absent():
   conn = get_db()
   with conn.cursor() as cur:
      classx = request.form['class']
      namex = request.form['name']
      statusx = request.form['status']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO absent(class,name,status,date,add_from)VALUES(%s,%s,%s,%s,%s)",(classx,namex,statusx,datex,add_fromx))
   conn.commit()
   return render_template("absent.html")

@app.route('/add_late',methods = ['POST'])
def add_late():
   conn = get_db()
   with conn.cursor() as cur:
      classx = request.form['class']
      namex = request.form['name']
      statusx = request.form['status']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO late(class,name,status,date,add_from)VALUES(%s,%s,%s,%s,%s)",(classx,namex,statusx,datex,add_fromx))
   conn.commit()
   return render_template("late.html")


@app.route('/add_bills',methods = ['POST'])
def add_bills():
   conn = get_db()
   with conn.cursor() as cur:
      invoice_typex = request.form['invoice_type']
      invoice_nox = request.form['invoice_no']
      descriptionx = request.form['description']
      amountx = request.form['amount']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO bills(invoice_type,invoice_no,description,amount,date,add_from)VALUES(%s,%s,%s,%s,%s,%s)",(invoice_typex,invoice_nox,descriptionx,amountx,datex,add_fromx))
   conn.commit()
   return render_template("bills.html")


@app.route('/add_income',methods = ['POST'])
def add_income():
   conn = get_db()
   with conn.cursor() as cur:
      namex = request.form['name']
      cprx = request.form['cpr']
      descriptionx = request.form['des']
      amountx = request.form['amount']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO income(name,cpr,description,amount,date,add_from)VALUES(%s,%s,%s,%s,%s,%s)",(namex,cprx,descriptionx,amountx,datex,add_fromx))
   conn.commit()
   return render_template("income.html")


@app.route('/add_salaries',methods = ['POST'])
def add_salaries():
   conn = get_db()
   with conn.cursor() as cur:
      namex = request.form['name']
      cprx = request.form['cpr']
      salaryx = request.form['salary']
      datex = request.form['date']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO salaries(name,cpr,salary,date,add_from)VALUES(%s,%s,%s,%s,%s)",(namex,cprx,salaryx,datex,add_fromx))
   conn.commit()
   return render_template("salaries.html")


@app.route('/add_employees',methods = ['POST'])
def add_employees():
   conn = get_db()
   with conn.cursor() as cur:
      namex = request.form['name']
      cprx = request.form['cpr']
      addressx = request.form['address']
      contactx = request.form['contact']
      salaryx = request.form['salary']
      joindatex = request.form['joindate']
      add_fromx = request.form['add_from']
      cur.execute("INSERT INTO employees(name,cpr,address,contact,salary,joindate,add_from)VALUES(%s,%s,%s,%s,%s,%s,%s)",(namex,cprx,addressx,contactx,salaryx,joindatex,add_fromx))
   conn.commit()
   return render_template("employees.html")
