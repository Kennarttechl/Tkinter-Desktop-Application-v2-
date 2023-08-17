"""HTTP Request Methods
=> ✅ GET
=> ✅ POST
=> ✅ PUT
=> ✅ HEAD
=> ✅ DELETE
=> ✅ PATCH
=> ✅ OPTIONS

            Some commonly used status codes. They are as follows:
• 200 OK means the request has been successful. The request could be a GET, PUT,
or PATCH.
• 201 Created means the POST request has been successful and a record has been
created.
• 204 No Content means the DELETE request has been successful.
• 400 Bad Request means there is something wrong with the client request. For
example, there is a syntax error in the JSON format.
• 401 Unauthorized means the client request is missing authentication details.
• 403 Forbidden means the requested resource is forbidden.
• 404 Not Found means the requested resource doesn't exist.


=> ✅ GET.....is used to request data from a specified resource
=> ✅ POST....is used to send data to a server to create/update a resource


=> ✅ requests: module help us to the get the data from any link
Jason module helps us to parse the data into human readable format
"""

import bcrypt
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask import Flask, jsonify, request



app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = '2a65c33c474054ddf21e'
client = MongoClient('mongodb://localhost:27017')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///api.db'
db = SQLAlchemy(app)
db = client.SentencesDatabase
users = db['Users']


bundle = {
    "coins": [
        {
            "id": 1,    
            "name": "Bitcoin",
            "price_usd": 10000,
            "symbol": "BTC"
                },
            {
            "name": "kenneth",
            "color": "brown"
        }
    ],
    "students_names": [
        "kenneth",
        "benjamin",
        "godwin"
    ],
    "attributes": {
        "name": "kenneth",
        "age": 25,
        "gender": "male",
        "occupation": "software engineer"
    }
}


@app.route('/')
@app.route('/home')
def home():
    return jsonify(bundle), 404


def check_posted_data(posted_data, function_name):
    if function_name in ["add", "subtract", "multiply"]:
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200

    elif function_name == "division":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data['y']) == 0:
            return 302
        else:
            return 200


def verify_pw(username, password):
    user = users.find_one({"Username": username})
    if user:
        hashed_pw = user["Password"]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_pw):
            return True
    return False


def count_tokens(username):
    user = users.find_one({"Username": username})
    if user:
        return user['Tokens']
    return 0


class Register(Resource):
    def post(self):
        posted_data = request.get_json()
        username = posted_data['username']
        password = posted_data['password']
        hashed_pw = bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())

        if users.find_one({"Username": username}):
            return jsonify({"status": 409, "message": "Username already exists"})

        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6
        })

        return jsonify({"status": 200, 
                        "message": "You have successfully signed up for the API"
                        })


class Store(Resource):
    def post(self):
        posted_data = request.get_json()
        username = posted_data['username']
        password = posted_data['password']
        sentence = posted_data['sentence']

        if not verify_pw(username, password):
            return jsonify({"status": 302, "message": "Invalid username or password"})

        num_tokens = count_tokens(username)
        if num_tokens <= 0:
            return jsonify({"status": 301, "message": "You have insufficient tokens"})

        users.update_one({"Username": username}, 
                         {
            "$set": {
                "Sentence": sentence, 
                "Tokens": num_tokens - 1}
        })

        return jsonify({"status": 200, "message": "Sentence saved successfully"})


class Add(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'add')
        if status_code != 200:
            return jsonify({"message": "An error occurred", "status_code": status_code})

        x = int(posted_data['x'])
        y = int(posted_data['y'])
        result = x + y

        return jsonify({"message": result, "status_code": 200})


class Subtract(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'subtract')
        if status_code != 200:
            return jsonify({"message": "An error occurred", "status_code": status_code})

        x = int(posted_data['x'])
        y = int(posted_data['y'])
        result = x - y

        return jsonify({"message": result, "status_code": 200})


class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'multiply')
        if status_code != 200:
            return jsonify({"message": "An error occurred", "status_code": status_code})

        x = int(posted_data['x'])
        y = int(posted_data['y'])
        result = x * y

        return jsonify({"message": result, "status_code": 200})


class Division(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'division')
        if status_code != 200:
            return jsonify({"message": "An error occurred", "status_code": status_code})

        x = int(posted_data['x'])
        y = int(posted_data['y'])

        if y == 0:
            return jsonify({"message": "Cannot divide by zero", "status_code": 302})

        result = x / y

        return jsonify({"message": result, "status_code": 200})


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Division, '/division')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

