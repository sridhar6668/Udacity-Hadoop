#!/usr/bin/python

import sys
import csv
# Read input one line at a time
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for data in reader:
        # some defensive programming. Make sure the line of length 5
	if(len(data) == 5):
        	user_id, reputation, gold, silver, bronze = data
	        print "{0}\t{1}\t{2}".format(user_id, "A", reputation)

        elif(len(data) == 19):
        	user_id = data[3]
        	post_id = data[0]
        	title = data[1]
	        print "{0}\t{1}\t{2}\t{3}".format(user_id, "B", post_id, title)
        
