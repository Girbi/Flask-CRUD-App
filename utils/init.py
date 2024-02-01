from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "alex1234"
app.config["MYSQL_DB"] = "pibd"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
