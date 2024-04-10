from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def greeting():
    return 'welcome'

@app.route('/welcome/home')
def home_greeting():
    return 'welcome home'

@app.route('/welcome/back')
def return_greeting():
    return 'welcome back'

