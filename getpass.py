#!/usr/bin/env python
# Description: read password with raw_input and don't write to stdout

# found at http://docs.python.org/2/library/termios.html
def my_getpass(prompt="Password: "):
	import termios, sys
	fd = sys.stdin.fileno()
	old = termios.tcgetattr(fd)
	new = termios.tcgetattr(fd)
	new[3] = new[3] & ~termios.ECHO          # lflags
	try:
		termios.tcsetattr(fd, termios.TCSADRAIN, new)
		passwd = raw_input(prompt)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old)
	sys.stdout.write('\n')
	sys.stdout.flush()
	return passwd

if __name__ == "__main__":
	print my_getpass()
