import api_fake_news
import cluster
from algorithm import calculate_trust_score
from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import *


NEUTRAL_POST_TRUST_SCORE = '50'


app = Flask(__name__)
CORS(app)


@app.route("/score/<post_id>", methods=['GET'])
def get_score(post_id):
    post_info = cluster.getPost(post_id)

    trust_score = calculate_trust_score(post_info)

    result = {}
    result['score'] = trust_score
    result['positive_votes'] = post_info['votesTrusted']
    result['negative_votes'] = post_info['votesUntrusted']
    result['model_prediction'] = post_info['modPred']

    return jsonify(result)


@app.route("/vote/<post_id>", methods=['POST'])
def vote(post_id):
    request_body = request.get_json()
    user_id = request_body.get("user_id")
    user_vote = int(request_body.get("vote"))
    
    if not user_id and not user_vote:
        return '', 400
    
    post_info = cluster.getPost(post_id)
    if not cluster.getVote(user_id, post_id) and not post_info['userID'] == user_id and (user_vote == -1 or user_vote == 1):
        cluster.insertVote(user_id, user_vote, post_id)
        update_post_vote_stats(user_id, user_vote, post_id, post_info)


@app.route("/<post_id>", methods=['PUT'])
def create_post(post_id):
    request_body = request.get_json()
    post_text = request_body.get("text", "")
    user_id = request_body.get("user_id", "")

    if not post_text or not user_id:
        return '', 400
    
    model_prediction = api_fake_news.classify_text(post_text)
    if not cluster.getPost(post_id):
        cluster.insertPost(post_id, model_prediction, user_id, 0, 0, 0, 0)
    return


@app.route("/<user_id>", methods=['PUT'])
def create_user(user_id):
    if not cluster.getUser(user_id):
        cluster.insertUser(user_id, False)
    return


@app.route('/<user_id>', method=['POST'])
def update_user_trust(user_id):
    request_body = request.get_json()
    is_trusted_user = request_body.get("isTrusted", "")
    if is_trusted_user:
        cluster.updateUser(user_id, is_trusted_user)
