from flask import Flask, request, render_template, redirect
import random, sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    print(randstring(200))
    if request.method == 'GET':
        return render_template('index.html')

def randstring(length):
    string = []
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(length):
        string.append(alph[random.randrange(51)])
    
    return "".join(string)