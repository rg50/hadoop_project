#!/usr/bin/python

import sys

tag_count = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the tag and val is the post length

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisTag, thisLen = data_mapped

	# Add up the lengths for each tag
	if thisTag in tag_count:
		tag_count[thisTag] += int(thisLen)
	else:
		tag_count[thisTag] = int(thisLen)

# Determine top ten highest value tags in the tag_count
Top_ten = sorted(tag_count.iteritems(), key=lambda (k, v): (-v, k))[:10]

# Print output
for i in Top_ten:
	print i[0], "\t", i[1]