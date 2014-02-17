#!/usr/bin/python

# Data set used is forum_node.tsv and contains post information

# We want four elements from the dataset: the node type, author_id, post_id and
# the abs_parent_id 
# For this, we'll output the author_id, node_type and post_id for questions and
# the author_id, node_type and abs_parent_id for answers

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
            print "{0}\t{1}\t{2}".format(author_id, word, post_id)