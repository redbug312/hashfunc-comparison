tilechart:
	cat data/studentID | ./hashfunc.py | ./tilechart.py

barchart:
	cat data/studentID | ./hashfunc.py | ./barchart.py

execute: tilechart
