import cluster

def buildDict(postID):
    user_votes = {}
    user_trust = {}
    for user in cluster.db.users.find():
        if postID in user['votes']:
            user_votes[user['name']] = user['votes']
    for user in cluster.db.users.find():
        if postID in user['trust']:
            user_trust[user['name']] = user['trust']
    return user_votes, user_trust

def heuristic(postId):
    user_votes, user_trust = buildDict()
    return cluster.heuristic(postId, user_votes, user_trust)
