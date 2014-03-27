#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running line by line

import subprocess as sub
import shlex

p = sub.Popen(shlex.split("python dummy_stdout.py"), stdout=sub.PIPE)
while True:
    line = p.stdout.readline()
    if line == '':
        break
    print line.rstrip()
