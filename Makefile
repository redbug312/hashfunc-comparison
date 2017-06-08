tilechart:
	cat data/studentID | ./hashfunc.py | ./tilechart.py -g

barchart:
	cat data/studentID | ./hashfunc.py | ./barchart.py -g

execute: barchart
