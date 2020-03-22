from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM book")
    allbook = cur.fetchall()
    cur.close()
    # return render_template('home.html',data = allbook)
    return str(allbook)


@app.route('/insert', methods = ['POST'])
def insert():
    inputdata=request.get_json()
    title = inputdata['title']
    page = inputdata['page']
    cur = mysql.connection.cursor()
    cur.execute(" insert into book (title,page) values('"+str(title)+"','"+str(page)+"')")
    mysql.connection.commit()
    cur.close()
    return {"result":"data inserted successfully"}


@app.route('/update',methods=['POST'])
def update():
    inputdata=request.get_json()
    title = inputdata['title']
    page = inputdata['page']
    cur = mysql.connection.cursor()
    query="UPDATE book SET title='"+str(title)+"', page='"+str(page)+"' WHERE id=1"
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return {"result":"data updated successfully"}


@app.route('/delete', methods = ['DELETE'])
def delete():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM book WHERE id=1")
    mysql.connection.commit()
    cur.close()
    return {"result":"data deleted successfully"}


if __name__ == "__main__":
    app.run(debug=True)
