tilechart:
	cat data/core7000.dict | ./hashfunc.py | ./tilechart.py

barchart:
	cat data/core7000.dict | ./hashfunc.py | ./barchart.py

execute: tilechart
