
from flask import Flask       # 載入 Flask
from flask import request      # 載入 request 物件
from flask import redirect     # 載入 redirect 函式
from flask import render_template  # 載入render_template 函式
from flask import session
from flask import url_for


runapp = Flask(__name__,static_folder = "public",static_url_path = "/") 

runapp.secret_key = b'\xe8s\xb9\x0e\xddZ \xc3\x80\xa5\x1a\x11\x99J\xe7V'

@runapp.route("/" )
def index():
    return render_template("signin.html")


@runapp.route("/signin", methods = ["POST"])
def signin():
    if request.values["account"]=="test"and request.values["password"]=="test":
        session["user"] = request.values["account"]
        # print(session["user"])
        return redirect("/member")
    return redirect("/error") 


@runapp.route("/member")
def success():
    if session.get("user"):
        return render_template("member.html")
    else:
        return redirect("/")

@runapp.route("/error")
def failure():
    return render_template("error.html")

@runapp.route("/signout")
def signout():
    session.pop("user",None)
    return redirect(url_for("index"))

runapp.run(port = 3000)

if __name__ == "__main__":  
    runapp.run()     
