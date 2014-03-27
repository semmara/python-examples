#!/usr/bin/env python
import subprocess as sub
import shlex

p = sub.Popen(shlex.split("python dummy_stdout.py"), stdout=sub.PIPE)
while True:
    line = p.stdout.readline()
    if line == '':
        break
    print line.rstrip()
