#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

user_table_user_id = 10
forum_table_user_id = None
reputation = -1

for line in sys.stdin:
        
	data = line.strip().split("\t")
	if(len(data) != 3 and len(data) != 4):
		continue
	category = data[1]
	if(category is "A"):
		user_table_user_id = data[0]
		reputation = data[2]
	elif(category is "B"):
		forum_table_user_id = data[0]
		post_id = data[2]
		#form_title = data[3]
		if(user_table_user_id == forum_table_user_id):
			print user_table_user_id, "\t", forum_table_user_id, "\t",reputation, "\t",post_id
		
	
		
	
