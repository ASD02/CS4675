from cluster import *


def update_post_vote_stats(user_id, user_vote, post_id, post_info):
    if getUser(user_id)['isTrustedUser']:
        votesTrusted = post_info['votesTrusted'] + 1
        avgTrusted = ((post_info["avgTrusted"] * post_info['votesTrusted']) + user_vote) / votesTrusted
        updatePostTrusted(post_id, votesTrusted, avgTrusted)
    else:
        votesUntrusted = post_info['votesUntrusted'] + 1
        avgUntrusted = ((post_info["avgUntrusted"] * post_info['votesUntrusted']) + user_vote) / votesUntrusted
        updatePostUntrusted(post_id, votesUntrusted, avgUntrusted)
