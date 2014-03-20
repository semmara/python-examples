#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running

import subprocess as sub
import sys
import select
import shlex

cmd = shlex.split("nc -l localhost 9966")
if len(sys.argv) > 1:
	cmd = sys.argv[1:]
p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)

l_r = [p.stdout.fileno(), p.stderr.fileno()]
while len(l_r) > 0:
	r,w,x = select.select(l_r, [], [])
	for i in r:
		if i is p.stdout.fileno():
			ch = p.stdout.read(1)
			if len(ch) == 0:
				l_r.remove(i)
			else:
				sys.stdout.write(ch)
				sys.stdout.flush()
		elif i is p.stderr.fileno():
			ch = p.stderr.read(1)
			if len(ch) == 0:
				l_r.remove(i)
			else:
				sys.stderr.write(ch)
				sys.stderr.flush()

