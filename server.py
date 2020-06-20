from flask import Flask, render_template,redirect

import logging


app = Flask(__name__)

#logeaza conexiunile cu orice device
logging.basicConfig(filename='demo.log', level=logging.DEBUG)

@app.route("/")
def lol():
    return redirect("/")

    
@app.route('/home')
def hello_world():
    return render_template('home_page.html')

@app.route("/Evenimente")
def event():
    return render_template("evt.html")

@app.route('/Profesori')

def prof():
    return render_template('prof.html')

@app.route('/Contact')
def cntact(): 
    return render_template('conact.html')


app.run(host = "192.168.0.150", debug=True)



"""
pentru a adauga certificat de ce o fi:
import cryptography
app.run(ssl_context = "adhoc")
Si  apoi dute in fiecare html template si schimba la link in loc de https sa fie http

"""