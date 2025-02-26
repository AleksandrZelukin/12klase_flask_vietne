# https://timeweb.cloud/tutorials/python/sozdanie-veb-prilozheniya-s-ispolzovaniem-python-flask#bd-dlya-loginov-i-parolej
from flask import Flask, render_template,request
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

db_lp = sqlite3.connect('login_password.db')
cursor_db = db_lp.cursor()
sql_create = '''CREATE TABLE IF NOT EXISTS passwords(
                login TEXT PRIMARY KEY,
                password TEXT NOT NULL);'''

cursor_db.execute(sql_create)
db_lp.commit()

cursor_db.close()
db_lp.close()

app=Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html",title="Sveiki!")
  
@app.route("/about")
def about():
  return render_template("about.html",title="PAR")

@app.route("/blog")
def blog():
  return render_template("blog.html",title="BLOGS") 

@app.route("/contact")
def contact():
  return render_template("contact.html",title="KONTAKTI")

@app.route("/auth_bad")
def bad():
  return render_template("auth_bad.html",title="Neveicmīga autorizacija")

@app.route('/registracija', methods=['GET', 'POST'])
def form_registration():

  if request.method == 'POST':
    Login = request.form.get('Login')
    Password = request.form.get('Password')

    db_lp = sqlite3.connect('login_password.db')
    cursor_db = db_lp.cursor()
    sql_insert = '''INSERT INTO passwords VALUES('{}','{}');'''.format(Login, Password)

    cursor_db.execute(sql_insert)
    db_lp.commit()

    cursor_db.close()
    db_lp.close()

    return render_template('successfulregis.html')

  return render_template('registration.html')


@app.route("/successfulauth")
def ok():
  return render_template("auth_bad.html",title="autorizacija izdevas")

@app.route("/autorizacija", methods=['GET', 'POST'])
def form_authorization():
   if request.method == 'POST':
      Login = request.form.get('Login')
      Password = request.form.get('Password')
      db_lp = sqlite3.connect('login_password.db')
      cursor_db = db_lp.cursor()
      cursor_db.execute(('''SELECT password FROM passwords
                                               WHERE login = '{}';
                                               ''').format(Login))
      pas = cursor_db.fetchall()

      cursor_db.close()
      try:
        if pas[0][0] != Password:
          return render_template('auth_bad.html')
      except:
        return render_template('auth_bad.html')

      db_lp.close()
      return render_template('successfulauth.html')

   return render_template('autorizacija.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)