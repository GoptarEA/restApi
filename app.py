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


# class Districts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
#
# class School(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     district = db.Column(db.Integer, db.ForeignKey('districts.id'))
#     pupils_amount = db.Column(db.Integer, nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    school = db.Column(db.String(20), unique=False, nullable=False)
    group = db.Column(db.String(4), unique=False, nullable=False)
    birth_date = db.Column(db.String(20), unique=False, nullable=False)

    def __init__(self, email, password, surname, name, school, group, birth_date):
        self.email = email
        self.password = password
        self.surname = surname
        self.name = name
        self.school = school
        self.group = group
        self.birth_date = birth_date





@app.route('/api/v1/register', methods=["POST", "GET"])
def register():
    try:
        u = User(request.args.get("email"),
                 generate_password_hash(request.args.get("password")),
                 request.args.get("name"),
                 request.args.get("surname"),
                 request.args.get("school"),
                 request.args.get("group"),
                 request.args.get("birth_date"))
        print(request.args.get("email"),
                 request.args.get("password"),
                 request.args.get("name"),
                 request.args.get("surname"),
                 request.args.get("school"),
                 request.args.get("group"),
                 request.args.get("birth_date"))
        db.session.add(u)
        db.session.flush()
        db.session.commit()
        return "Аккаунт успешно зарегистрирован"
    except:
        return "Что-то пошло не так"


@app.route('/api/v1/auth', methods=["POST", "GET"])
def auth():
    email = request.args.get("email")
    password = request.args.get("password")
    user = [person for person in User.query.all() if person.email == email]
    if user and check_password_hash(user[0].password, password):
        return f'success {user[0].name} ' \
               f'{user[0].surname} ' \
               f'{user[0].school} ' \
               f'{user[0].group} ' \
               f'{user[0].birth_date} ' \
               f'{user[0].email}'
    return "access denied"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90)
