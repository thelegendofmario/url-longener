from flask import Flask, request, render_template, redirect
from markupsafe import escape
import random, sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    
    db = sqlite3.connect("urls.db")
    curs = db.cursor()
# with app.request_context():
    if request.method == 'GET':
        return render_template('index.html')

    url = request.form.get("url")
    #print(url)
#print(globslug)
    slug = randslug(len(url)+random.randrange(100, 300))
    data = (slug, url)
    
    curs.execute("INSERT INTO urls(slug, og) VALUES(?, ?)", data)
    db.commit()
    #print(globslug)
    
    return render_template('index.html', globslug=slug).encode("utf-8")

@app.route("/<wslug>")
def redir(wslug):
    db = sqlite3.connect("urls.db")
    curs = db.cursor()
    to_slug = escape(wslug)
    all_data_request = curs.execute("SELECT * FROM urls")
    all_data = all_data_request.fetchall()
    for i in all_data:
        if i[0] == to_slug:
            return redirect(f"https://{i[1]}")
        
    return render_template('fail.html')




def randslug(length):
    return randstring(length+random.randrange(100,200))

def randstring(length):
    string = []
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz😀😃😄😁😆😅😂🤣🥲🥹☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳🙂‍↕️😏😒🙂‍↔️😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🫣🤗"
    for i in range(length):
        string.append(alph[random.randrange(len(alph)-1)])

    return "".join(string)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)