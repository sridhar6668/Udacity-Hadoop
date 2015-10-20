#!/usr/bin/python

import sys

oldKey = None
value = 0;
count = 0;
for line in sys.stdin:
        
	data = line.strip().split("\t")
	if(len(data) != 3):
		continue
	
	#thisKey, dataType, length = data;
	if data[1] == "A":
		
		questionPostId = data[0]
		questionLength = data[2]

		if oldKey:
			if count != 0:
				print oldKey, "\t", oldQuestionnLength,  "\t", value/count
			else:
				print oldKey, "\t", oldQuestionnLength,  "\t", 0;
		oldKey = questionPostId;
		oldQuestionnLength = questionLength		
		count = 0;
		value = 0;

	if data[1] == "B":
		questionPostId = data[0]
		answerLength = data[2]
		value += int(answerLength)
		count += 1
		
if oldKey:
	if count != 0:
		print oldKey, "\t", oldQuestionnLength,  "\t", value/count
	else:
		print oldKey, "\t", oldQuestionnLength,  "\t", 0;
	
			
'''
	thisKey, hour = data		
	if oldKey and oldKey!=thisKey:
		max = 0
		maxHour = -1
		for i in range(0,24):
			if(hourArr[i] > max):
				maxHour = i + 1
				max = hourArr[i]
		for i in range(0,24):
			if(hourArr[i] == max and max > 0):	
				print oldKey, "\t", i+1
		hourArr = [0] * 24
	oldKey = thisKey
	if(hour.isdigit() and int(hour) < 24 and int(hour) > 0):
		hourArr[int(hour) - 1] += 1
	
if oldKey:
	max = 0
	maxHour = -1
	for i in range(0,24):
		if(hourArr[i] > max):
			max = hourArr[i]
	for i in range(0,24):
		if(hourArr[i] == max and max > 0):
			print oldKey, "\t", i+1
'''				
	
		
	
