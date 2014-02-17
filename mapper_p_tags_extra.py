#!/usr/bin/python

# Data set used is forum_node.tsv and contains post information

# We want two elements from the dataset:  the node type and the tags
# For this, we'll output each tag as a key with a value of the post length
# These will only be output for those observations that are questions

# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')

for line in reader:
	if len(line) == 19:
		tags = line[2].split()
		post_len = len(line[4])
		for i in tags:
			print "{0}\t{1}".format(i, post_len)