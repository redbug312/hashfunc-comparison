tilechart:
	cat data/studentID | ./hashfunc.py | ./tilechart.py

histogram:
	cat data/studentID | ./hashfunc.py | ./histogram.py -g

execute: tilechart
