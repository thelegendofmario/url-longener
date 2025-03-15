from flask import Flask, request, render_template, redirect
from markupsafe import escape
import random, sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    db = sqlite3.connect("urls.db")
    curs = db.cursor()
    if request.method == 'GET':
        return render_template('index.html')
    url = request.form.get("url")
    #print(url)
    #print(globslug)
    globslug = randslug(len(url)+random.randrange(300, 500))
    
    #print(globslug)
    return render_template('index.html', globslug=globslug)

@app.route("/<wslug>")
def redir(wslug):
    return f"<h1>hello, {escape(wslug)}</h1>"




def randslug(length):
    return randstring(length+random.randrange(300,500))

def randstring(length):
    string = []
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz😀😃😄😁😆😅😂🤣🥲🥹☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳🙂‍↕️😏😒🙂‍↔️😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🫣🤗"
    for i in range(length):
        string.append(alph[random.randrange(len(alph)-1)])

    return "".join(string)