#!/usr/bin/env python
import subprocess as sub

p = sub.Popen(['cat', 'popen_realtime_output_simple.py'], stdout=sub.PIPE)
while True:
    line = p.stdout.readline()
    if line == '':
        break
    print line.rstrip()
