import requests
from flask import Flask,render_template,request
import psycopg2

app= Flask(__name__)

conn = psycopg2.connect(database="service_db",
user="postgres", password="1111", host="localhost", port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html',error='')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None or (len(username) == 0 or len(password) == 0):
        return render_template('login.html', error='login or password is empty')

    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records)<=0:
        return render_template('login.html', error='user is not found')
    return render_template('account.html', full_name=records[0][1],login=records[0][2],password=records[0][3])



if __name__ == '__main__':
    app.run()

