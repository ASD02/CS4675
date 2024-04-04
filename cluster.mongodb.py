from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb+srv://adithdevakonda:CS4675@cluster0.dlwhjzr.mongodb.net/')
db = client['Cluster0']

# Method to insert data into the sites collection
def insertSites(siteName, siteURL, siteData, siteVotes):
    db.sites.insert_one({
        'name': siteName,
        'url': siteURL,
        'data': siteData,
        'votes': siteVotes
    })

# Method to update the votes of a site
def updateVotes(siteName, newVotes):
    db.sites.update_one(
        {'name': siteName},
        {'$set': {'votes': newVotes}}
    )

# Method to delete a site from the collection
def deleteSite(siteName):
    db.sites.delete_one({'name': siteName})

# Method to get a site by name
def getSite(siteName):
    return db.sites.find_one({'name': siteName})

# Method to insert user into the Users collection
def insertUser(userName, userVotes):
    db.users.insert_one({
        'name': userName,
        'votes': userVotes
    })

# Method to update the votes of a user
def updateUser(userName, newVotes):
    db.users.update_one(
        {'name': userName},
        {'$set': {'votes': newVotes}}
    )

# Method to delete a user from the collection
def deleteUser(userName):
    db.users.delete_one({'name': userName})

# Method to get a user by name
def getUser(userName):
    return db.users.find_one({'name': userName})

# Method to add a vote into the votes collection
def insertVote(userName, siteName, vote):
    db.votes.insert_one({
        'user': userName,
        'site': siteName,
        'vote': vote
    })

# Method to update a vote in the votes collection
def updateVote(userName, siteName, newVote):
    db.votes.update_one(
        {'user': userName, 'site': siteName},
        {'$set': {'vote': newVote}}
    )

# Method to delete a vote from the collection
def deleteVote(userName, siteName):
    db.votes.delete_one({'user': userName, 'site': siteName})

# Method to get a vote by user and site
def getVote(userName, siteName):
    return db.votes.find_one({'user': userName, 'site': siteName})

# Method to get all votes by user
def getVotesByUser(userName):
    return db.votes.find({'user': userName})

# Method to get all votes by site
def getVotesBySite(siteName):
    return db.votes.find({'site': siteName})