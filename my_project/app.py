from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.test


@app.route('/')
def model_insert():
    id = db.insert({
        'title': request.json['title'],
        'body': request.json['body'],
        'tags': request.json['tags'],
        'date': datetime.now()
    })
    return jsonify(str(ObjectId(id)))


@app.route('/write', methods=['POST'])
def model_insert():
    id = db.insert({
        'title': request.json['title'],
        'body': request.json['body'],
        'tags': request.json['tags'],
    })
    return jsonify(str(ObjectId(id)))