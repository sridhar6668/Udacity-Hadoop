#!/usr/bin/python

import sys

oldKey = None
hourArr = [0] * 24

for line in sys.stdin:
        
	data = line.strip().split("\t")
	if(len(data) != 2):
		continue

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
				
	
		
	
