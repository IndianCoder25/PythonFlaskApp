from flask import *;
import mysql.connector as conn
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("HomePage.html")

@app.route('/create_form')
def create_form():
    return render_template("CreateForm.html")

@app.route('/create',methods = ['POST'])
def create():
    con = conn.connect(host='localhost',database='python_db',user='root',password='root',charset='utf8',port=3307)
    cursor = con.cursor()
    sql = 'insert into students values(%s,%s,%s,%s)'
    li=[]
    for key,value in request.form.items():
        li.append(value)
    value = tuple(li)
    cursor.execute(sql,value)
    con.commit()
    return render_template("HomePage.html",message="Data Inserted !")

@app.route('/retrieve',methods = ['GET'])
def retrieve():
    con = conn.connect(host='localhost',database='python_db',user='root',password='root',charset='utf8',port=3307)
    cursor = con.cursor()
    sql= "select * from students"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("Retrieve.html",message=result)

@app.route('/delete/<enrollment>',methods = ['GET','POST'])
def delete(enrollment):
    con = conn.connect(host='localhost',database='python_db',user='root',password='root',charset='utf8',port=3307)
    cursor = con.cursor()
    sql= "delete from students where Enrollment=%s"
    value=(enrollment,)
    cursor.execute(sql,value)
    con.commit()
    return redirect("http://localhost:5000/retrieve")

@app.route('/update_form/<enrollment>')
def update_form(enrollment):
    con = conn.connect(host='localhost',database='python_db',user='root',password='root',charset='utf8',port=3307)
    cursor = con.cursor()
    sql= "select * from students where Enrollment=%s"
    value=(enrollment,)
    cursor.execute(sql,value)
    result = cursor.fetchall()
    return render_template("UpdateForm.html",message=result)

@app.route('/update/<enrollment>',methods = ['POST'])
def update(enrollment):
    con = conn.connect(host='localhost',database='python_db',user='root',password='root',charset='utf8',port=3307)
    cursor = con.cursor()
    sql= "update students set Name=%s,Email=%s,Password=%s where Enrollment=%s"
    li=[]
    for key,value in request.form.items():
        if(key == "enrollment"):
            pass
        else:
            li.append(value)
    li.append(enrollment)
    value = tuple(li)
    cursor.execute(sql,value)
    con.commit()
    return redirect("http://localhost:5000/retrieve")

if __name__ == '__main__':
    app.run(debug=True)