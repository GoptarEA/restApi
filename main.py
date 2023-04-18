from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from waitress import serve


app = Flask(__name__)
CORS(app)


app.secret_key = '1F7VkTpXpSBo9P6Oskv9Kq$23QwD9FG44U'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    school = db.Column(db.Integer, db.ForeignKey('school.id'))
    group = db.Column(db.String(4), unique=False, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, password, surname, name, school, group, birth_date):
        self.email = email
        self.password = password
        self.surname = surname
        self.name = name
        self.school = school
        self.group = group
        self.birth_date = birth_date


# class Districts(db.Model):
#     pass
#
#
# class School(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     district = db.Column(db.Integer, db.ForeignKey('districts.id'))
#     pupils_amount = db.Column(db.Integer, nullable=False)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    a = request.args.get("key1")
    if a == "2098":
        return "success"
    else:
        return "access denied"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # serve(app, host='0.0.0.0', port=8080, threads=1)
