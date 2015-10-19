#!/usr/bin/python

import sys
import csv
from datetime import datetime
# Read input one line at a time
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for data in reader:
        # some defensive programming. Make sure the line of length 19
        if(len(data) == 19):
        	user_id = data[3]
		if(user_id.isdigit()):
	        	date = data[8]
			temp = date.strip().split(" ")
			temp1 = temp[1].strip().split(":")
		        print "{0}\t{1}".format(user_id, temp1[0])
        
