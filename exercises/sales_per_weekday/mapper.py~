#!/usr/bin/python
import sys
from datetime import datetime
    # read standard input line by line
for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
    data = line.strip().split("\t")

        # some defensive programming. make sure the data array has only 6 items
    if(len(data) == 6):
        date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)
            # Now print out the data that will be passed to the reducer
