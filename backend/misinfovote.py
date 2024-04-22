import time
import api_fake_news
import cluster
from algorithm import calculate_trust_score
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_caching import Cache
from utils import *


app = Flask(__name__)
CORS(app)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 60})
cache.init_app(app)


@app.route("/score/<post_id>", methods=['GET'])
@cache.cached(timeout=60)
def get_score(post_id):
    start_ = time.time()
    post_info = cluster.getPost(post_id)

    if not post_info:
        return '', 400

    trust_score = calculate_trust_score(post_info)

    result = {}
    result['score'] = trust_score
    result['model_prediction'] = post_info['modPred']
    end_ = time.time()

    print(f"get_score took {end_ - start_} seconds")

    return jsonify(result), 200


@app.route("/vote", methods=['POST'])
def vote():
    start_ = time.time()
    request_body = request.get_json()
    post_id = request_body.get("post_id", "")
    user_id = request_body.get("user_id", "")
    user_vote = request_body.get("vote", "")
    
    post_info = cluster.getPost(post_id)

    if not post_id or not user_id or not user_vote or not cluster.getUser(user_id) or not post_info:
        return '', 400
    
    user_vote = int(user_vote)
    
    if not cluster.getVote(user_id, post_id) and not post_info['userID'] == user_id and (user_vote == -1 or user_vote == 1):
        cluster.insertVote(user_id, user_vote, post_id)
        update_post_vote_stats(user_id, user_vote, post_id, post_info)
    end_ = time.time()

    print(f"vote took {end_ - start_} seconds")

    return '', 200


@app.route("/posts/<post_id>", methods=['PUT'])
def create_post(post_id):
    request_body = request.get_json()
    post_text = request_body.get("text", "")
    user_id = request_body.get("user_id", "")

    if not post_text or not user_id or not cluster.getUser(user_id):
        return '', 400

    model_prediction = api_fake_news.classify_text(post_text)
    if not cluster.getPost(post_id):
        cluster.insertPost(post_id, model_prediction, user_id, 0, 0, 0, 0)
    return '', 200


@app.route("/users/<user_id>", methods=['PUT'])
def create_user(user_id):
    if not cluster.getUser(user_id):
        cluster.insertUser(user_id, False)
    return '', 200


@app.route('/trust/<user_id>', methods=['POST'])
def update_user_trust(user_id):
    request_body = request.get_json()
    is_trusted_user = request_body.get("isTrusted", "")
    if is_trusted_user and cluster.getUser(user_id):
        cluster.updateUser(user_id, is_trusted_user)
    return '', 200
