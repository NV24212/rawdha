from flask import Flask, render_template, url_for, request
import psycopg2

app = Flask(__name__)



@app.route("/")
def index():
   return render_template("index.html")

#1
@app.route('/add_cash',methods = ['POST'])
def add_cash():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO cash(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#2
@app.route('/add_account_receivable',methods = ['POST'])
def add_account_receivable():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO account_receivable(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#3
@app.route('/add_inventory',methods = ['POST'])
def add_inventory():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO inventory(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#4
@app.route('/add_building_and_lands',methods = ['POST'])
def add_building_and_lands():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO building_and_lands(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#5
@app.route('/add_cars_and_motors',methods = ['POST'])
def add_cars_and_motors():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO cars_and_motors(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")



#6
@app.route('/add_fixture_and_furniture',methods = ['POST'])
def add_fixture_and_furniture():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO fixture_and_furniture(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#7
@app.route('/add_account_payable',methods = ['POST'])
def add_account_payable():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO account_payable(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#8
@app.route('/add_accruals_expenses',methods = ['POST'])
def add_accruals_expenses():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO accruals_expenses(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#9
@app.route('/add_bonds',methods = ['POST'])
def add_bonds():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO bonds(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")





#10
@app.route('/add_loan',methods = ['POST'])
def add_loan():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO loan(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#11
@app.route('/add_net_income',methods = ['POST'])
def add_net_income():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO net_income(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#12
@app.route('/add_retained_earning',methods = ['POST'])
def add_retained_earning():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO retained_earning(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#13
@app.route('/add_other_income_non_operation',methods = ['POST'])
def add_other_income_non_operation():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO other_income_non_operation(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")



#14
@app.route('/add_sales_non_operation',methods = ['POST'])
def add_sales_non_operation():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO sales_non_operation(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")




#15
@app.route('/add_other_income_operation',methods = ['POST'])
def add_other_income_operation():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO other_income_operation(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")




#16
@app.route('/add_sales_operation',methods = ['POST'])
def add_sales_operation():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO sales_operation(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")



#17
@app.route('/add_product',methods = ['POST'])
def add_product():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO product(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#18
@app.route('/add_service',methods = ['POST'])
def add_service():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO service(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")

#19
@app.route('/add_electricity',methods = ['POST'])
def add_electricity():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO electricity(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")




#20
@app.route('/add_rent',methods = ['POST'])
def add_rent():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO rent(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


#21
@app.route('/add_salaries',methods = ['POST'])
def add_salaries():

   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   date = request.form['date']
   description = request.form['description']
   debt = request.form['debt']
   credit = request.form['credit']
   cur.execute("INSERT INTO salaries(date,description,debt,credit)VALUES(%s,%s,%s,%s)",(date,description,debt,credit))
   conn.commit()
   cur.close()
   conn.close()
   return render_template("index.html")


@app.route('/show',methods = ['GET'])
def show():
#1
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From cash")
   cash_debt = cur.fetchone()[0]


   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From cash")
   cash_credit = cur.fetchone()[0]

# 2
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From account_receivable")
   account_receivable_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From account_receivable")
   account_receivable_credit = cur.fetchone()[0]


# 3
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From inventory")
   inventory_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From inventory")
   inventory_credit = cur.fetchone()[0]

# 4
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From building_and_lands")
   building_and_lands_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From building_and_lands")
   building_and_lands_credit = cur.fetchone()[0]

# 5
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From cars_and_motors")
   cars_and_motors_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From cars_and_motors")
   cars_and_motors_credit = cur.fetchone()[0]


# 6
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From fixture_and_furniture")
   fixture_and_furniture_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From fixture_and_furniture")
   fixture_and_furniture_credit = cur.fetchone()[0]


# 7
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From loan")
   loan_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From loan")
   loan_credit = cur.fetchone()[0]

# 8
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From bonds")
   bonds_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From bonds")
   bonds_credit = cur.fetchone()[0]


# 9
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From accruals_expenses")
   accruals_expenses_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From accruals_expenses")
   accruals_expenses_credit = cur.fetchone()[0]

# 10
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From account_payable")
   account_payable_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From account_payable")
   account_payable_credit = cur.fetchone()[0]

# 11
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From retained_earning")
   retained_earning_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From retained_earning")
   retained_earning_credit = cur.fetchone()[0]


# 12
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From net_income")
   net_income_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From net_income")
   net_income_credit = cur.fetchone()[0]



# 13
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From sales_operation")
   sales_operation_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From sales_operation")
   sales_operation_credit = cur.fetchone()[0]

# 14
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From sales_non_operation")
   sales_non_operation_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From sales_non_operation")
   sales_non_operation_credit = cur.fetchone()[0]


# 15
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From other_income_operation")
   other_income_operation_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From other_income_operation")
   other_income_operation_credit = cur.fetchone()[0]

# 16
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From other_income_non_operation")
   other_income_non_operation_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From other_income_non_operation")
   other_income_non_operation_credit = cur.fetchone()[0]

# 17
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From service")
   service_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From service")
   service_credit = cur.fetchone()[0]


# 18
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From product")
   product_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From product")
   product_credit = cur.fetchone()[0]

# 19
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From electricity")
   electricity_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From electricity")
   electricity_credit = cur.fetchone()[0]

# 20
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From salaries")
   salaries_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From salaries")
   salaries_credit = cur.fetchone()[0]

# 21
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(debt) From rent")
   rent_debt = cur.fetchone()[0]
   conn = psycopg2.connect(database="count", user="postgres", password="0000", host="localhost", port="5432")
   cur = conn.cursor()
   cur.execute("SELECT SUM(credit) From rent")
   rent_credit = cur.fetchone()[0]


   total_debt = cash_debt + account_receivable_debt + inventory_debt + building_and_lands_debt + cars_and_motors_debt + fixture_and_furniture_debt + loan_debt + bonds_debt + accruals_expenses_debt + account_payable_debt + retained_earning_debt + net_income_debt + sales_operation_debt + sales_non_operation_debt + other_income_operation_debt + other_income_non_operation_debt + service_debt + product_debt + electricity_debt + salaries_debt + rent_debt

   total_credit = cash_credit + account_receivable_credit + inventory_credit + building_and_lands_credit + cars_and_motors_credit + fixture_and_furniture_credit + loan_credit + bonds_credit + accruals_expenses_credit +account_payable_credit + retained_earning_credit + net_income_credit + sales_operation_credit + sales_non_operation_credit + other_income_operation_credit + other_income_non_operation_credit + service_credit + product_credit + electricity_credit + salaries_credit + rent_credit




   return render_template("view/show.html",
   cash_debt=cash_debt,  
   cash_credit=cash_credit,
   account_receivable_debt=account_receivable_debt,
   account_receivable_credit= account_receivable_credit,
   inventory_debt = inventory_debt,
   inventory_credit = inventory_credit,
   building_and_lands_debt = building_and_lands_debt,
   building_and_lands_credit = building_and_lands_credit, 
   cars_and_motors_debt = cars_and_motors_debt,
   cars_and_motors_credit = cars_and_motors_credit,
   fixture_and_furniture_debt = fixture_and_furniture_debt,
   fixture_and_furniture_credit = fixture_and_furniture_credit,
   loan_debt = loan_debt,
   loan_credit = loan_credit,
   bonds_debt = bonds_debt,
   bonds_credit = bonds_credit,
   accruals_expenses_debt = accruals_expenses_debt,
   accruals_expenses_credit = accruals_expenses_credit,
   account_payable_debt = account_payable_debt,
   account_payable_credit = account_payable_credit,
   retained_earning_debt = retained_earning_debt,
   retained_earning_credit = retained_earning_credit,
   net_income_debt = net_income_debt,
   net_income_credit = net_income_credit,
   sales_operation_debt = sales_operation_debt,
   sales_operation_credit = sales_operation_credit,
   sales_non_operation_debt = sales_non_operation_debt,
   sales_non_operation_credit = sales_non_operation_credit,
   other_income_operation_debt = other_income_operation_debt,
   other_income_operation_credit = other_income_operation_credit,
   other_income_non_operation_debt = other_income_non_operation_debt,
   other_income_non_operation_credit = other_income_non_operation_credit,
   service_debt = service_debt,
   service_credit = service_credit,
   product_debt = product_debt,
   product_credit = product_credit,
   electricity_debt = electricity_debt,
   electricity_credit = electricity_credit,
   salaries_debt = salaries_debt,
   salaries_credit = salaries_credit,
   rent_debt = rent_debt,
   rent_credit = rent_credit,
   total_debt = total_debt,
   total_credit = total_credit
   )
   





if __name__ == "__main__":
   app.run(debug=True)