#!/usr/bin/env python
import time
import sys

for i in range(5):
    sys.stdout.write("a.")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("b.")
    sys.stdout.flush()
    time.sleep(0.5)
    print "bla"
    time.sleep(1.0)

