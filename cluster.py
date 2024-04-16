from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb+srv://adithdevakonda:CS4675@cluster0.dlwhjzr.mongodb.net/')
db = client['Cluster0']

# Method to insert data into the post collection
def insertPost(postID, modPred, userID, trustScore):
    db.posts.insert_one({
        'postID': siteName,
        'siteURL': siteURL,
        'userID': userID,
        'trustScore': trustScore
    })

# Method to update the votes of a post
def updateVotes(postID, trustScore):
    db.posts.update_one(
        {'postID': postID},
        {'trustScore': trustScore}
    )

# Method to delete a post from the collection
def deletePost(postID):
    db.posts.delete_one({'postID': postID})

# Method to get a site by name
def getPost(postID):
    return db.sites.find_one({'postID': postID})

# Method to insert user into the Users collection
def insertUser(userID, userTrustScore, isTrustedUser):
    db.users.insert_one({
        'userID': userID,
        'userTrustScore': userTrustScore,
        'isTrustedUser': isTrustedUser
    })

# Method to trust score the votes of a user
def updateUser(userID, userTrustScore, isTrustedUser):
    db.users.update_one(
        {'userID': userID},
        {'userTrustScore': userTrustScore},
        {'isTrustedUser': isTrustedUser}
    )

# Method to delete a user from the collection
def deleteUser(userID):
    db.users.delete_one({'userID': userID})

# Method to get a user by ID
def getUser(userID):
    return db.users.find_one({'userID': userID})

# Method to add a vote into the votes collection
def insertVote(userID, siteName, vote, postID, voteID):
    db.votes.insert_one({
        'user': userID,
        'site': siteName,
        'vote': vote,
        'postID': postID,
        'voteID': voteID
    })

# Method to update a vote in the votes collection
def updateVote(userID, postID, vote, voteID):
    db.votes.update_one(
        {'user': userID, 'postID': postID},
        {'vote': vote},
        {'voteID': voteID}
    )

# Method to delete a vote from the collection
def deleteVote(userID, postID):
    db.votes.delete_one({'user': userID, 'postID': postID})

# Method to get a vote by user and post
def getVote(userID, postID):
    return db.votes.find_one({'user': userID, 'postID': postID})

# Method to get all votes by user
def getVotesByUser(userID):
    return db.votes.find({'user': userID})

# Method to get all votes by post
def getVotesByPost(postID):
    return db.votes.find({'post ID': postID})