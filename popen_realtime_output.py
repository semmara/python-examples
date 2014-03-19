#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running

import subprocess as sub
import sys
import time as t
import select

p = sub.Popen(sys.argv[1:], stdout=sub.PIPE)

while True:
	select.select([p.stdout.fileno()], [], [])
	ch = p.stdout.read(1)
	if len(ch) == 0:
		break
	sys.stdout.write(ch)
	sys.stdout.flush()
	
