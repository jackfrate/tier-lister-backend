from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
from tinydb import TinyDB, Query


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
            return {
                'error': 'error'
            }
    elif request.method == 'POST':
        tier_list = request.json
        id = len(db.all())
        tier_list['id'] = id
        db.insert(tier_list)
        return {'message': 'success'}
