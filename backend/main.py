from flask import Flask,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="AhsanUmer"

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/covid'
db=SQLAlchemy(app)

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

@app.route("/")
def home():
    return render_template("index.html")

# testing that database is connected or not
@app.route("/test")
def test():
    try:
        a=Test.query.all()
        print(a)
        return "MY DATABASE IS CONNECTED"
    except Exception as e:
        print(e)
        return 'MY DATABASE IS NOT CONNECTED'
app.run(debug=True)
