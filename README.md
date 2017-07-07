# hashfunc-comparison
Test collision resistency non-cryptographic hash functions.
This is the experience part of project for 2017 NTU CSIE Probability lecture.

![](https://s3.amazonaws.com/media-p.slid.es/uploads/396189/images/3908294/Figure_1-14.png)

## Presentation part
* slide: [XOR8 hash function](https://slides.com/redbug312/xor8-hash-function)

We uses some optimizations to have **xor8** hash behaves as good as **djb2**, even in less time.

```shell
$ ./hashfunc.py --hash xor8 data/studentID | ./barchart.py -g
$ ./hashfunc.py --hash djb2 data/studentID | ./barchart.py -g

# Optimization 1
$ ./hashfunc.py --hash xor8 --size 64 data/studentID | ./barchart.py -g

# Optimization 2
$ ./hashfunc.py --hash xor8 --size 64 --regroup data/studentID | ./tilechart.py -g

# Optimization 3
$ ./hashfunc.py --hash xor8 --size 64 --regroup --hist-eq=0,6 data/studentID | ./tilechart.py -g
```

Notice that the data is slightly transforned due to privacy, thus the result would behaves different from the slide above. But there’s the same effect on each optimization.

## Structure
The program can also be used to analyze other hash functions. `hashfunc.py` will read lines in file given as first argument, printing out a hashtable. `barchart.py` and `tilechart.py` will read the hashtable and show the responding chart.

1. Options in `hashfunc.py`
    * `-h`, `--hash`: specify the hash function, **sum8, xor8, djb2** is implemented
    * `-s`, `--size`: specify the bucket number in the hashtable
    * `-r`, `--regroup`: specify whether to use shift folding, suitable only for `data/studentID` now
    * `-e`, `--hist-eq`: specify the subscription for each line to perform histogram equilization
2. Options in `barchart.py`, `tilechart.py`
    * `-g`: specify using pyplot to show the chart, instead of terminal

And it will show the distribution of djb2 hashing result from every line in the file `studentID`

## Environments
* Python3 with numpy, matplotpy installed

## References
* [HASHING](https://www.csie.ntu.edu.tw/~hsinmu/courses/_media/dsa_12spring/hashing.pdf)
* [Which hashing algorithm is best for uniqueness and speed?](https://softwareengineering.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed) | StackExchange
* [Gaussian Distribution + Hash Tables](https://stackoverflow.com/questions/4324490/gaussian-distribution-hash-tables?rq=1) | StackOverflow
* [Why are 5381 and 33 so important in the djb2 algorithm?](https://stackoverflow.com/questions/1579721/why-are-5381-and-33-so-important-in-the-djb2-algorithm)
