#!/usr/bin/python
from __future__ import division
import sys


user_responses = {}
user_answer_score = {}
oldKey = None
post_auth = None
count = 0

# Loop around the data
# It will be in the format key\tval1\tval2
# Where key is the post_id, val1 is the node type and val2 is the author


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisType, thisAuth = data_mapped

    # Add post's author and indication of whether q was answered to dict
    # if new post key doesn't match last row
    if oldKey and oldKey != thisKey:
        if count >= 1:
            question_answered = 1
        else:
            question_answered = 0
        if post_auth in user_responses:
            user_responses[post_auth].append(int(question_answered))
        else:
            user_responses[post_auth] = [question_answered]
        count = 0
        oldkey = thisKey

    # Determine the author of the post question and count number of answers
    oldKey = thisKey
    if thisType == 'question':
        post_auth = thisAuth
    if thisType == 'answer':
        count += 1

# Add last item to dictionary
if count >= 1:
    question_answered = 1
else:
    question_answered = 0
if post_auth in user_responses:
    user_responses[post_auth].append(question_answered)
else:
    user_responses[post_auth] = [question_answered]

# Determine answer percentage score and number of questions for each user 
# that asked a question
for user in user_responses:
    num_questions = len(user_responses[user])
    num_answers = sum(user_responses[user])
    answer_percentage = num_answers / num_questions
    user_answer_score[user] = [answer_percentage, num_questions]

# Get a sorted list of users from lowest to highest answer perecentage
users_sorted = sorted(user_answer_score.iteritems(), key=lambda (k, v): (v[0], k))

# Print output in order for users with at least 5 questions asked
print "User", "\t", "Percentage of Questions Answered", "\t", "Questions Asked"
for i in users_sorted:
    if i[1][1] >= 5:
        print i[0], "\t", i[1][0], "\t", i[1][1]

