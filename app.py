from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    
    return "Hello Flask, on Azure App Service for Linux \n 2 teste"
     


