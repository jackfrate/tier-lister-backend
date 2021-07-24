from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import json

tier_lists = []
test_list = {"name": "the_original", "id": 0, "sTier": [], "aTier": [], "bTier": [], "cTier": [{"url": "", "name": "test"}], "dTier": [], "eTier": [], "fTier": [], "noTier": []}
tier_lists.append(test_list)

app = Flask(__name__)
api = Api(app)


@app.route('/tier-list-list', methods=['GET'])
def handle_tier_list():
    ret = list(map(create_list_item, tier_lists))
    return jsonify(ret)


@app.route('/tier-list/<int:id>', methods=['GET', 'POST'])
def get_tier_list():
    if request.method == 'GET':
        try:
            tl_id = request.args.get('id')
            return tier_lists[tl_id]
        except:
            return {
                'error': 'error'
            }
    elif request.method == 'POST':
        tier_list = request.json
        id = len(tier_lists)
        tier_list['id'] = id
        tier_lists.append(tier_list)


#
# helper functions
#


def create_list_item(tl):
    return {
        'id': tl['id'],
        'name': tl['name']
    }
