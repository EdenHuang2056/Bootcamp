
from flask import Flask
from flask import request      # 載入 request 物件
from flask import redirect     # 載入 redirect 函式
from flask import render_template  # 載入render_template 函式
from flask import session
from flask import url_for
import mysql.connector


runapp = Flask(__name__, static_folder="static", static_url_path="/")

runapp.secret_key = b'\xe8s\xb9\x0e\xddZ \xc3\x80\xa5\x1a\x11\x99J\xe7V'


mydb = mysql.connector.connect(
    host="127.0.0.1",
    username="root",
    password="!nctu820228",
    database="website"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myhome")

# mycursor.execute("SHOW DATABASES")

# insert
# sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)"
# val = (request.values["name"], request.values["username"], request.values["password"])
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# select
# mycursor.execute("SELECT * FROM user")
# result = mycursor.fetchall()

# delete
# sqle = "DELETE * FROM user"
# mycursor.execute(sqle)

# print(result)

# # print(mydata)



@runapp.route("/" )
def index():
    return render_template("signin.html")


@runapp.route("/signup", methods = ["POST"])
def signup():

    # abc = request.values["username"]
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
    # print("SELECT username FROM user where username = "+str(request.values['username']))
    # print("SELECT username FROM user where username = request.values['username']")
    # print(result)
    # print((str(request.values["username"]),))
    # print(request.values["username"])

    # if (str(request.values["username"]),) not in result:
        # sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)"
        # val = (str(request.values["name"]), str(request.values["username"]), str(request.values["password"]))
        # mycursor.execute(sql, val)
        # mydb.commit()
        # return render_template("signin.html")
    # else:
    #     return redirect("/error/?message=帳號已被註冊")

@runapp.route("/signin", methods = ["POST"])
def signin():
    session["username"] = request.values["username"]
    # user=request.values["username"]
    session["password"] = request.values["password"]
    # pas = request.values["password"]

    # print(user)
    # print(type(user))
    # print(type(str(user)))
    # print(str(user))
    # print(request.values["username"])
    # print(request.values["password"])

    mycursor.execute(f"SELECT name,username,password FROM user where username='{request.form['username']}'")
    result1 = mycursor.fetchone()
    # print(result1)
    # for i in range(len(result1)):
    # print(type(result1[i][1]))
    if result1[1] == request.values["username"] and result1[2] == request.values["password"]:
        session["name"] = result1[0]
        # print(result1)
        return redirect("/member")
    else:    
        return redirect("/error/?message=帳號與密碼錯誤")
    # if request.values["username"]=="test"and request.values["password"]=="test":
        # session["username"] = request.values["username"]
        # session["password"] = request.values["password"]
        # session["name"] = se
        # print(session["user"])
        # sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)"
        # val = ("peter", request.values["username"], request.values["password"])
        # mycursor.execute(sql, val)
        # mydb.commit()
    # return redirect("/member")
        # return redirect("/error")
    # return redirect("/error/?message=帳號與密碼錯誤")


@runapp.route("/member")
def success():
    if session.get("username"):
        return render_template("member.html",nametitle=session["name"])
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

runapp.run(port = 3000)

if __name__ == '__main__':
    main()

