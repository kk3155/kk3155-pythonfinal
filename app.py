# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
     return render_template("index.html")
@app.route("/ENGI1006")
def ENGI1006():
    #return "<p> This is my <b> ENGI1006 </b> website! </p>"
    return render_template("1006.html")
@app.route("/Kriti")
def Kriti():
    return "My name is Kriti Kumar."
#start the server
if __name__ == "__main__":
    app.run()
