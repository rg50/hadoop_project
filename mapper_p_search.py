#!/usr/bin/python

# Data set used is forum_node.tsv and contains post information

# We want three elements from the dataset: the post, the post_id and the author_id
# For this, we'll output the author_id, each word in the post and the post_id

# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')

for line in reader:
    if len(line) == 19:
        body = line[4].split(" ")
        post_id = line[0]
        author_id = line[3]
        for word in body:
            print "{0}\t{1}\t{2}".format(author_id, word.lower(), post_id)