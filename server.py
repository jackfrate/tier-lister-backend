from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
from tinydb import TinyDB, Query

SUCCESS_MESSAGE = {'message': 'success'}
FAILURE_MESSAGE = {'message': 'error', 'error': 'error'}

app = Flask(__name__)
CORS(app)
api = Api(app)

db = TinyDB('./db.json')


@app.route('/tier-list-list', methods=['GET'])
def handle_tier_list():
    return jsonify(db.all())


@app.route('/tier-list/<int:id>', methods=['GET'])
@app.route('/tier-list', methods=['POST'])
def get_tier_list(id: int = None):
    if request.method == 'GET':
        try:
            TierList = Query()
            return jsonify(db.search(TierList.id == id)[0])
        except:
            return FAILURE_MESSAGE
    elif request.method == 'POST':
        tier_list = request.json
        id = len(db.all())
        tier_list['id'] = id
        db.insert(tier_list)
        return SUCCESS_MESSAGE


@app.route('/tier-list/<int:id>', methods=['DELETE'])
def delete_single_list(id: int):
    try:
        TierList = Query()
        db.remove(TierList.id == id)
        message = SUCCESS_MESSAGE
        message['message'] = f'deleted tier list id: {id}'
        return message
    except:
        return FAILURE_MESSAGE


@app.route('/delete-all', methods=['DELETE'])
def delete_all():
    db.truncate()
