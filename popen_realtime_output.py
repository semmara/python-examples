#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running

import subprocess as sub
import sys
#import select
import shlex

cmd = shlex.split("nc -l localhost 9966")
if len(sys.argv) > 1:
	cmd = sys.argv[1:]
p = sub.Popen(cmd, stdout=sub.PIPE)

while True:
	#select.select([p.stdout.fileno()], [], [])
	ch = p.stdout.read(1)
	if len(ch) == 0:
		break
	sys.stdout.write(ch)
	sys.stdout.flush()
	
