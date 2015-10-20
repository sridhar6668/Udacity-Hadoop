#!/usr/bin/python

import sys
import csv
from datetime import datetime
# Read input one line at a time
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

question = "question"
answer = "answer"
for data in reader:
        # some defensive programming. Make sure the line of length 19
        if(len(data) == 19):
		postType = data[5];
		if(postType == question):
	        	post_id = data[0]
			sentence = data[4]
		        print "{0}\t{1}\t{2}".format(post_id, "A", len(sentence))
		if(postType == answer):
			question_id = data[6]
			sentence = data[4]
		        print "{0}\t{1}\t{2}".format(question_id, "B", len(sentence))
		
        
