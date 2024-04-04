import cluster

def buildDict():
    user_votes = {}
    user_trust = {}
    for user in cluster.db.users.find():
        user_votes[user['name']] = user['votes']
    for user in cluster.db.users.find():
        user_trust[user['name']] = user['trust']
    return user_votes, user_trust

def heuristic(postId):
    user_votes, user_trust = buildDict()
    return cluster.heuristic(postId, user_votes, user_trust)