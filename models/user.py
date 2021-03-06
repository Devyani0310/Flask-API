import sqlite3
from flask_restful import Resource,reqparse
from db import db

class UserModel(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=id).first()

# class UserRegister(Resource):

#     parser = reqparse.RequestParser()
#     parser.add_argument('username', 
#             type=str,
#             required=True,
#             help="This field cannot be blank"
#     )
#     parser.add_argument('password',
#             type=str,
#             required=True,
#             help="This field cannot be blank"
#     )

#     def post(self):
#         data = UserRegister.parser.parse_args()

#         if UserModel.find_by_username(data['username']):
#             return {'message': "This user already exists"},400

#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "INSERT INTO users VALUES (NULL,? ,?)"
#         cursor.execute(query, (data['username'], data['password']))
        
#         connection.commit()
#         connection.close()

#         return {'message': "User created succefully"},201