from cluster import getUser


nlp_weight = 0.3

# Weights for trusted source
t_trusted_voter = 0.35
t_untrusted_voter = 0.25
t_source = 0.1

# Weights for untrusted source
u_trusted_voter = 0.40
u_untrusted_voter = 0.3


def calculate_trust_score(post_info) -> int:
    trusted_average = post_info['avgTrusted']
    untrusted_average = post_info['avgUntrusted']
    nlp_model_score = post_info['modPred']

    if nlp_model_score == 0:
        # If opinion, do not score the post
        return -1
    else:
        # Calculate the overall trust score
        if getUser(post_info['userID'])['isTrustedUser']:
            overall_trust_score = (
                (trusted_average * t_trusted_voter) +
                (untrusted_average * t_untrusted_voter) +
                (nlp_model_score * nlp_weight) +
                t_source
            )
        else:
            overall_trust_score = (
                (trusted_average * u_trusted_voter) +
                (untrusted_average * u_untrusted_voter) +
                (nlp_model_score * nlp_weight)
            )

        # range 0 - 100
        return int(((overall_trust_score + 1) / 2) * 100)


def heuristic(nlp_model_prediction: int, user_votes: dict, user_trust: dict) -> int:
    '''
    user_votes = {
        'trusted_user_id_1': 1,
        'trusted_user_id_2': -1,
        'untrusted_user_id_1': 1,
        'untrusted_user_id_2': 1,
    }

    user_trust = {
        'trusted_user_id_1': True,
        'trusted_user_id_2': True,
        'untrusted_user_id_1': False,
        'untrusted_user_id_2': False,
    }
    '''

    # Initialize variables
    trusted_votes = []
    untrusted_votes = []

    # Separate the votes based on trustworthiness
    for user_id, vote in user_votes.items():
        if user_trust[user_id]:
            trusted_votes.append(vote)
        else:
            untrusted_votes.append(vote)

    # weighted average for trusted and untrusted votes
    trusted_average = sum(trusted_votes) / len(trusted_votes) if trusted_votes else 0
    untrusted_average = sum(untrusted_votes) / len(untrusted_votes) if untrusted_votes else 0

    # weights
    trusted_weight = 0.35
    untrusted_weight = 0.15
    nlp_weight = 0.5

    # NLP model prediction to a score
    # TODO: Figure out how to score an opinion
    if nlp_model_prediction > 0:
        nlp_model_score = 1 
    else:
        nlp_model_score = -1

    # Calculate the overall trust score
    overall_trust_score = (
        (trusted_average * trusted_weight) +
        (untrusted_average * untrusted_weight) +
        (nlp_model_score * nlp_weight)
    )

    # range 0 - 100
    normalized_trust_score = int(((overall_trust_score + 1) / 2) * 100)

    return normalized_trust_score
