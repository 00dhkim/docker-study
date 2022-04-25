import time
import datetime
import sys
print('start!')
for _ in range(1000):
	print(datetime.datetime.now())
	with open('file/text.txt') as f:
		lines = f.readlines()
		print('stdout', lines, flush=True)
		print('stderr', lines, file=sys.stderr, flush=True)
	time.sleep(3)

