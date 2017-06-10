# hashfunc-comparison
Test collision resistency non-cryptographic hash functions.
This is a part of project for 2017 NTU CSIE Probability lecture.

## How to use
In your terminal:
```
$ ./hashfunc.py -f data/studentID | ./tilechart.py
```

And it will show the distribution of djb2 hashing result from every line in the file `studentID`

## Environments
* Python3 with numpy, matplotpy installed
