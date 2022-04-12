from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash #para hashear la contrasena
from bson import json_util #para convertir la respuesta desde mongo en un json
from bson.objectid import ObjectId #para buscar en mongo con el id pasando de string a object
from flask_cors import CORS, cross_origin #para poder usar en local host ambos servidores a la vez


app = Flask(__name__)

CORS(app)

app.config['MONGO_URI']='mongodb://127.0.0.1:27017/practica3db'

mongo = PyMongo(app)

@cross_origin
@app.route('/students', methods=['GET'])
def get_students():
    student = mongo.db.students.find()
    response = json_util.dumps(student)
    return Response(response, mimetype='application/json')

@cross_origin
@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student = mongo.db.students.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(student)
    #return response si retorno asi se envia en formato string, abajo tiene formato json
    return Response(response, mimetype='application/json')

@cross_origin
@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    mongo.db.students.delete_one({'_id': ObjectId(id)})
    response = jsonify({'messsage': ' student ' + id + ' was delete'})
    return response

@cross_origin
@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    authenticated = request.json['authenticated']
    current_focus_time = request.json['current_focus_time']
    current_break_time = request.json['current_break_time']
    record_focus_time = request.json['record_focus_time']
    if name  and email and username and password and authenticated and current_focus_time and current_break_time and record_focus_time:
        #por ahora validando que hay datos
        hashed_password = generate_password_hash(password)
        #escondiendo la contrasena
        mongo.db.students.update_one({'_id': ObjectId(id)}, {'$set':{
            'name': name,
            'email': email,
            'username': username,
            'password': hashed_password,
            'authenticated': authenticated,
            'current_focus_time': current_focus_time,
            'current_break_time': current_break_time,
            'record_focus_time': record_focus_time
        }})
        response = jsonify({'messsage': ' student ' + id + ' was updated'})
        return response
    else:
        return not_found()

@cross_origin
@app.route('/students', methods=['POST'])
def create_student():
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    authenticated = request.json['authenticated']
    current_focus_time = request.json['current_focus_time']
    current_break_time = request.json['current_break_time']
    record_focus_time = request.json['record_focus_time']
    #atrapando los datos de request
    if name  and email and username and password and authenticated and current_focus_time and current_break_time and record_focus_time:
        #por ahora validando que hay datos
        hashed_password = generate_password_hash(password)
        #escondiendo la contrasena
        id = mongo.db.students.insert_one({
            'name': name,
            'email': email,
            'username': username,
            'password': hashed_password,
            'authenticated': authenticated,
            'current_focus_time': current_focus_time,
            'current_break_time': current_break_time,
            'record_focus_time': record_focus_time
            })
        #guardando los datos del request
        response = {
            'id': str(id),
            'name': name,
            'username': username,
            'email': email,
            'password': hashed_password,
            'authenticated': authenticated,
            'current_focus_time': current_focus_time,
            'current_break_time': current_break_time,
            'record_focus_time': record_focus_time
        }
        return response
    else:
        return not_found()

@cross_origin
@app.errorhandler(404)
def not_found(error=None):
    message = jsonify({
    'message': 'Resource Not Found: ' + request.url,
    'status': '404'
    })
    message.status_code=404
    return message


if __name__=="__main__":
	app.run(debug=True)