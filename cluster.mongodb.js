// Select the database to use.
use('Cluster0');

//method to insert data into the sites collection
function insertSites(siteName, siteURL, siteData, siteVotes) {
  db.getCollection('sites').insertOne({
    name: siteName,
    url: siteURL,
    data: siteData,
    votes: siteVotes
  });
}

//method to update the votes of a site
function updateVotes(siteName, newVotes) {
  db.getCollection('sites').updateOne(
    { name: siteName },
    { $set: { votes: newVotes } }
  );
}

//method to delete a site from the collection
function deleteSite(siteName) {
  db.getCollection('sites').deleteOne({ name: siteName });
}

//method to get a site by name
function getSite(siteName) {
  return db.getCollection('sites').findOne({ name: siteName });
}

//method to insert user into the Users collection
function insertUser(userName, userVotes) {
  db.getCollection('users').insertOne({
    name: userName,
    votes: userVotes
  });
}

//method to update the votes of a user
function updateUser(userName, newVotes) {
  db.getCollection('users').updateOne(
    { name: userName },
    { $set: { votes: newVotes } }
  );
}

//method to delete a user from the collection
function deleteUser(userName) {
  db.getCollection('users').deleteOne({ name: userName });
}

//method to get a user by name
function getUser(userName) {
  return db.getCollection('users').findOne({ name: userName });
}

//method to add a vote into the votes collection
//votes are: -2 for definitely fake news, -1 for probably fake news, 0 for unsure, 1 for probably real news, 2 for definitely real news
function insertVote(userName, siteName, vote){
  db.getCollection('votes').insertOne({
    user: userName,
    site: siteName,
    vote: vote
  });
}

//method to update a vote in the votes collection
function updateVote(userName, siteName, newVote){
  db.getCollection('votes').updateOne(
    { user: userName, site: siteName },
    { $set: { vote: newVote } }
  );
}

//method to delete a vote from the collection
function deleteVote(userName, siteName){
  db.getCollection('votes').deleteOne({ user: userName, site: siteName });
}

//method to get a vote by user and site
function getVote(userName, siteName){
  return db.getCollection('votes').findOne({ user: userName, site: siteName });
}

//method to get all votes by user
function getVotesByUser(userName){
  return db.getCollection('votes').find({ user: userName });
}

//method to get all votes by site
function getVotesBySite(siteName){
  return db.getCollection('votes').find({ site: siteName });
}
