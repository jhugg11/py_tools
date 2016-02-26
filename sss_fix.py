from datetime import datetime
from dateutil import parser

filename = raw_input("enter the filename: ")

f = open(filename)

lines = f.readlines()
for l in lines:
	print l[1:7]
f.close()
