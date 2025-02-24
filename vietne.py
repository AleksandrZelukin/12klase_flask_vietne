# https://timeweb.cloud/tutorials/python/sozdanie-veb-prilozheniya-s-ispolzovaniem-python-flask#bd-dlya-loginov-i-parolej
from flask import Flask, render_template


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

@app.route("/autorizacija")
def autorizacija():
  return "Šeit autorizētie lietotāji varēs pieteikties vietnes privātajā daļā."

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)