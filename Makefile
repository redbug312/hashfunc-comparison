tilechart:
	./hashfunc.py data/studentID | ./tilechart.py -g

barchart:
	./hashfunc.py data/studentID | ./barchart.py -g

execute: barchart
