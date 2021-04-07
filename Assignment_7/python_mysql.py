
from flask import Flask
from flask import request      
from flask import redirect     
from flask import render_template  
from flask import session
from flask import url_for
import mysql.connector
import json


runapp = Flask(__name__, static_folder="static", static_url_path="/")

runapp.secret_key = b'\xe8s\xb9\x0e\xddZ \xc3\x80\xa5\x1a\x11\x99J\xe7V'


mydb = mysql.connector.connect(
    host= ,
    username= ,
    password= ,
    database=
)

mycursor = mydb.cursor()


# delete
# sqle = "DELETE * FROM user"
# mycursor.execute(sqle)



@runapp.route("/" )
def index():
    return render_template("signin.html")


@runapp.route("/signup", methods = ["POST"])
def signup():

    mycursor.execute(f"SELECT * FROM user where username ='{request.values['username']}'")
    result = mycursor.fetchone()
    if result:
        return redirect("/error/?message=帳號已被註冊")
    else:
        sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)"
        val = (str(request.values["name"]), str(request.values["username"]), str(request.values["password"]))
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("signin.html")
    

@runapp.route("/signin", methods = ["POST"])
def signin():
    session["username"] = request.values["username"]
    session["password"] = request.values["password"]

    mycursor.execute(f"SELECT name,username,password FROM user where username='{request.form['username']}'")
    result1 = mycursor.fetchone()

    if result1[1] == request.values["username"] and result1[2] == request.values["password"]:
        session["name"] = result1[0]
        return redirect("/member")
    else:    
        return redirect("/error/?message=帳號與密碼錯誤")
    

@runapp.route("/member")
def success():
    request.args.get("username")
    if session.get("username"):
        return render_template("member.html",nametitle=session["name"] )
    else:
        return redirect("/")


@runapp.route("/error/")
def failure():
    msgtxt=request.args.get("message")
    return render_template("error.html")

@runapp.route("/signout")
def signout():
    session.pop("user",None)
    return redirect(url_for("index"))


@runapp.route("/api/user")
def search():

    searchname = request.args.get("username", None)

    # print(searchname)

    mycursor.execute(f"SELECT * FROM user where username='{searchname}'")
    result2 = mycursor.fetchone()
    # print(result2)
    if result2 is None:
        dic = {}
        dic['"data"'] = "null"
        return json.dumps(dic, ensure_ascii=False)

    else:  
        id = result2[0]
        name = result2[1]
        username = result2[2]

        dic = {}
        detail = {'id':id,'name':name,'username':username}
        dic['data'] = detail

        return json.dumps(dic, ensure_ascii=False)
    


runapp.run(port = 3000)



