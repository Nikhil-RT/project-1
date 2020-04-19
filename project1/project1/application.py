import os
from flask import Flask, session,render_template,request,flash,redirect,url_for,logging
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from create import User,db

app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
def main():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["GET","POST"])
def register():

    if (request.method == "POST"):
        mail = request.form['name']
        key = request.form['pwd']

        count = User.query.filter_by(email=mail).count()
        print (count)
        try:
            register = User(email=mail, password=key)
            db.session.add(register)
            db.session.commit()
            a=User.query.all()
            print(a)
            return render_template("login.html",name=mail)
        except:
            error="You have already registered with this email"
            return render_template("register.html",message=error)
    return render_template("register.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
    return render_template("login.html")


@app.route("/admin")
def admin():
    users=User.query.all()

    return render_template ("admin.html",data=users)

# if __name__ == "__main__":
#     print ("main not called")
with app.app_context():
    print ("main called")
    main()