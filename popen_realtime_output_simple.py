#!/usr/bin/env python
import subprocess as sub

p = sub.Popen(['python', 'stdout_dummy.py'], stdout=sub.PIPE)
while True:
    line = p.stdout.readline()
    if line != '':
        print line.rstrip()
    else:
        break
