#!/usr/bin/env python
# Author: semmara
# Description: print output while subprocess is still running

import subprocess as sub
import sys
import shlex
import thread
import select
import time
import os
from tempfile import TemporaryFile

import threading
import socket

class T(threading.Thread):
    _shutdown_msg = "shutdown"

    def __init__(self):
        threading.Thread.__init__(self)
        self._fd = TemporaryFile()
        self._comm_fd = TemporaryFile()
        self._run = False

    def get_file_handle(self):
        return self._fd

    def run(self):
        self._run = True
        while self._run:
            t1 = time.time()
            r, _, _ = select.select([self._fd.fileno(), self._comm_fd.fileno()], [], [])
            print "select time:", time.time()-t1
            for elem in r:
                if elem == self._fd.fileno():
                    s = self._fd.tell()
                    self._fd.seek(0, os.SEEK_END)  # to the end
                    e = self._fd.tell()
                    if s == e:  # nothing new
                        continue
                    self._fd.seek(-(e-s), os.SEEK_END)
                    diff = self._fd.read(e-s)
                    if True:
                        sys.stdout.write(diff)
                        sys.stdout.flush()

                # exit
                elif elem == self._comm_fd.fileno():
                    self._comm_fd.seek(0, os.SEEK_END)
                    if self._comm_fd.tell() == len(T._shutdown_msg):
                        self._run = False
        self._comm_fd.write(T._shutdown_msg)
        self._comm_fd.flush()

    def stop(self):
        self._comm_fd.seek(0, os.SEEK_END)
        if self._comm_fd.tell() != 0:
            return
        self._comm_fd.write(T._shutdown_msg)
        self._comm_fd.flush()
        while self._comm_fd.tell() != 2*len(T._shutdown_msg):
            self._comm_fd.seek(0, os.SEEK_END)

    def __del__(self, ):
        self._fd.close()


cmd = shlex.split("nc -l localhost 9966")
if len(sys.argv) > 1:
    cmd = sys.argv[1:]


t = T()
p = sub.Popen(cmd, stdout=t.get_file_handle())

#stdout_lock = thread.allocate_lock()

#
#def t_read(stream):
#    while True:
#        r, _, _ = select.select([stream.fileno()], [], [])
#        for elem in r:
#            if elem == stream.fileno():
#                s = stream.tell()
#                stream.seek(0, os.SEEK_END)  # to the end
#                e = stream.tell()
#                if s == e:
#                    continue
#                    #return
#                stream.seek(-(e-s), os.SEEK_END)
#                ch = stream.read(e-s)
#        #       ch = stream.read(1)
#                if len(ch) == 0:
#                    return
#                with stdout_lock:
#                    sys.stdout.write(ch)
#                    sys.stdout.flush()

t.start()

#thread.start_new_thread(t_read, (f,))
#thread.start_new_thread(t_read, (p.stderr,))

print "WAIT"
p.wait()
t.stop()
print "END"
time.sleep(2.0)
