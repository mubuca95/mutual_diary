from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://liebe:21212121@localhost/mutual_diary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False' #turns of flask extension's behaviour(davranış)
app.secret_key = "mbc"
api = Api(app)
jwt = JWT(app, authenticate,identity)
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host = '192.168.0.16',port = 9010, debug = True)


