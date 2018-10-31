from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import uuid

db_connect = create_engine('sqlite:///oasis.db')
app = Flask(__name__)
api = Api(app)

class Questions(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from questions") # This line performs query and returns json result
        return {'questions': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} # Fetches first column that is Employee ID

    #TO DO:  Support for HTML and images in base64

class Users(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        last_name = request.json['last_name']
        first_name = request.json['first_name']
        email = request.json['email']
        sessionId = str(uuid.uuid4())
        query = conn.execute("insert into users values (null,'{0}','{1}','{2}','{3}')".format(last_name,first_name,email,sessionId))
        return {'status': 'success', 'sessionId': sessionId}

    #TO DO:  Detection if the email already exists, to create "logins" that may many sessions associated
    #TO DO:  Add code to ensure UUID is unique, just random now

class Tests(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        sessionId = request.json['sessionId']
        userId = request.json['userId']
        answer1 = request.json['answer1']
        answer2 = request.json['answer2']
        answer3 = request.json['answer3']
        query = conn.execute("insert into tests values (null,'{0}','{1}','{2}','{3}','{4}')".format(sessionId,userId,answer1,answer2,answer3))
        return {'status': 'Success - Final Assessment Questions have been Submitted!'}


    #TO DO:  Save per question rather than needing them all to be submitted

#Routes
api.add_resource(Questions, '/questions')
api.add_resource(Users, '/users')
api.add_resource(Tests, '/tests')

if __name__ == '__main__':
     app.run(port='5002')
