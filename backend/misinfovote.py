import api_fake_news
import cluster
from algorithm import heuristic
from flask import Flask, jsonify, request
from flask_cors import CORS


NEUTRAL_POST_TRUST_SCORE = '50'


app = Flask(__name__)
CORS(app)


@app.route("/score/<post_id>", methods=['GET'])
def get_score(post_id):
    user_votes_raw = cluster.getVotesByPost(post_id)
    user_votes = {}
    for _vote in user_votes_raw:
        user_votes[_vote['user']] = _vote["vote"]
    users_raw = cluster.getUsers([_vote['user'] for _vote in user_votes_raw])
    user_trust_scores = {}
    for _user in users_raw:
        user_trust_scores[_user['userID']] = _user["userTrustScore"]
    model_prediction = cluster.getPost(post_id)['modPred']

    result = {}
    result['score'] = heuristic(model_prediction, user_votes, user_trust_scores)
    result['positive_votes'] = sum([1 for _ in user_votes if user_votes[_] > 0])
    result['negative_votes'] = len(user_votes) - result["positive_votes"]
    result['model_prediction'] = model_prediction

    return jsonify(result)


@app.route("/vote/<post_id>", methods=['POST'])
def vote(post_id):
    request_body = request.get_json()
    user_id = request_body.get("user_id")
    user_vote = request_body.get("vote")
    if not cluster.getVote(user_id, post_id) and not cluster.getPost(post_id)['userID'] == user_id :
        cluster.insertVote(user_id, user_vote, post_id)
    return

@app.route("/<post_id>", methods=['PUT'])
def create_post(post_id):
    request_body = request.get_json()
    post_text = request_body.get("text")
    user_id = request_body.get("user_id")
    model_prediction = api_fake_news.classify_text(post_text)
    if not cluster.getPost(post_id):
        cluster.insertPost(post_id, model_prediction, user_id, NEUTRAL_POST_TRUST_SCORE)
    return

@app.route("/<user_id>", methods=['PUT'])
def create_user(user_id):
    if not cluster.getUser(user_id):
        cluster.insertUser(user_id, 0, False)
    return
