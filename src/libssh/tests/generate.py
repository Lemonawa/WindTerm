#!/usr/bin/python
import os
a = "".join(chr(i % 256) for i in xrange(4096))
while True:
	try:
		os.write(1,a)
	except:
		exit(0)
