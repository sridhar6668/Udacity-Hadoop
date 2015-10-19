#!/usr/bin/python
import sys

salesTotal = 0
oldKey = None
count = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    

    if oldKey and oldKey != thisKey:
      print oldKey, "\t", (salesTotal/count)
      oldKey = thisKey
      salesTotal = 0
      count = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count+=1
# print the last value
if oldKey != None:
    print oldKey, "\t", (salesTotal/count)
