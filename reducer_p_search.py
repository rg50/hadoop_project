#!/usr/bin/python

import sys

oldKey = None
userIndex = {}

# Loop around the data
# It will be in the format key\tval\tval2
# Where key is the author_id, val is a word and val2 is the post 
# associated with that word
#


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisWord, thisPost = data_mapped

    # Add word or post id to inverted index for each user
    if thisKey in userIndex:
        if thisWord in userIndex[thisKey]:
            userIndex[thisKey][thisWord].append(thisPost)
        else:
            userIndex[thisKey][thisWord] = [thisPost]
    else:
        userIndex[thisKey] = {thisWord : [thisPost]}


# Print out User Id, word and posts
for user in userIndex:
    for word in userIndex[user]:
        print user, "/t", word, "/t", userIndex[user][word]

