#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running

import subprocess as sub
import sys
import shlex
import thread
import select

cmd = shlex.split("nc -l localhost 9966")
if len(sys.argv) > 1:
	cmd = sys.argv[1:]
p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)

stdout_lock = thread.allocate_lock()
def t_read(stream):
	while True:
		r, _, _ = select.select([stream.fileno()], [], [])
                for elem in r:
                        if elem == stream.fileno():
				ch = stream.read(1)
				if len(ch) == 0:
					return
				with stdout_lock:
					sys.stdout.write(ch)
					sys.stdout.flush()

thread.start_new_thread(t_read, (p.stdout,))
thread.start_new_thread(t_read, (p.stderr,))
p.wait()

