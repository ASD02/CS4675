import random
from time import time
from algorithm import calculate_trust_score
from cluster import *
from api_fake_news import classify_text

texts = [
    "Wayde van Niekerk duly qualified for the World Championship 400 meters final on Sunday but the defending champion and world record holder looks to have a real battle on his hands after some searing semi-final performances. The South African was desperately trying to conserve energy as he bids for a 200/400m double but was forced to go deeper than he would have liked by Botswana's Baboloki Thebe in the second of three semi-finals, eventually clocking 44.22 seconds.",
    "Bill Clinton went on the Conan show and spewed bitterness towards President Trump At one point, he insinuated that Trump is a  member of the dictator s Club . He and Conan are both guilty of slamming our president while he's overseas trying to deal with the North Koreans and Chinese. The left will never stop with their bashing of Trump on a very personal level",
    "House Speaker Paul Ryan is a snake, a hypocrite, and a weasel. He is also an incredible coward. Part of being a public servant is listening to the people. However, that is definitely not a value that Speaker Ryan shares. On Friday, Planned Parenthood advocates showed up at his Capitol Hill offices, only to be greeted with guards at every turn. It seemed that Ryan and his cronies were expecting the people to show up, sporting their pink  I Stand With Planned Parenthood  shirts, with boxes and boxes of petitions in tow, signed by tens of thousands of Americans who are demanding answers to Ryan s plans to take away healthcare from millions of American women.When the advocates were blocked by Capitol Hill police, finally a staffer had to escort them to Ryan s office. When they got there, the door was locked and heavily guarded. There was a sign that read, Please knock, only scheduled appointments will be admitted.",
    "Egyptian authorities have accused Reuters and the BBC of inaccurate coverage of clashes in the western desert between security forces and armed militants in which police officers and conscripts were killed on Friday. In a statement, Egypt's State Information Service (SIS) said Reuters had made grave professional mistakes  by relying on unidentified security sources and not  resorting to official security authorities to get correct information. The Ministry of Interior in an initial statement on Friday did not give any casualty figure for Friday s clashes. On Saturday, a ministry statement said 16 police and conscripts were killed and another 13 wounded in a remote western desert area after they came under heavy fire from the armed group. However, three security sources told Reuters as many as 52 police had been killed in gun battles, which security sources said involved militants firing rockets at a police convoy.",
    "The food at this restaurant was awful. Never going back again!"
]

times__ = []
times = 0
for _ in range(5):
    start_ = time()
    classify_text(texts[_])
    end_ = time()
    times += (end_ - start_)
    times__.append(end_ - start_)

print(f"Average time to classify texts is {times/5} seconds")
print(times__)

times = 0
for _ in range(5):
    post_id_ = str(random.randint(50, 100))
    post_info = getPost(post_id_)
    start_ = time()
    calculate_trust_score(post_info)
    end_ = time()
    times += (end_ - start_)

print(f"Average time to calculate trust scores is {times/5} seconds")

times = 0
for _ in range(5):
    post_id = str(random.randint(11150, 11200))
    user_id = str(random.randint(1115, 1120))
    modPred = random.choice([-1, 0, 1])
    votesTrusted = random.randint(0, 10)
    avgTrusted = random.uniform(-1, 1)
    votesUntrusted = random.randint(0, 1110)
    avgUntrusted = random.uniform(-1, 1)
    start_ = time()
    insertPost(post_id, modPred, user_id, votesTrusted, avgTrusted, votesUntrusted, avgUntrusted)
    end_ = time()
    times += (end_ - start_)

print(f"Average time to insert a post in the DB is {times/5} seconds")

times = 0
for _ in range(5):
    post_id = str(random.randint(11150, 11200))
    user_id = str(random.randint(1115, 1120))
    vote = random.choice([-1, 1])
    start_ = time()
    insertVote(user_id, vote, post_id)
    end_ = time()
    times += (end_ - start_)

print(f"Average time to insert a vote in the DB is {times/5} seconds")