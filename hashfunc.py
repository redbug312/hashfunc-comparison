#! /usr/bin/python3
""" Hash every inputs to generate a hashtable
"""

from operator import add, xor
from functools import reduce
from collections import Counter
import numpy

# parse functions: string -> bytes=[int]
bytelist = lambda line: list(map(int, line.strip().split()))
raw_str  = lambda line: bytes(line.strip(), 'utf-8')
sID_int  = lambda line: [int(line[0:3], 16), int(line[3:6], 16), int(line[6:9], 16)]
sID_HE   = lambda line, he: [he(line[0:6]), int(line[6:9], 16)]

# hash functions: bytes=[int] -> int
sum8 = lambda bytes_: reduce(add, bytes_) % (2 ** 32)
xor8 = lambda bytes_: reduce(xor, bytes_)
djb2 = lambda bytes_: reduce(lambda prev, curr: (prev * 33 + curr) % (2 ** 32), bytes_, 5381)

def generate_hashtable(keys, hashfunc, bucket):
    """ Generate the hashtable from given arguments
    Args:
        keys: [bytes] / [[int]]
        hashfunc: bytes -> int
        bucket: int
    Returns:
        [[string]]
    """
    hashtable = [[] for _ in range(bucket)]
    for key in keys:
        index = hashfunc(key) % bucket
        hashtable[index].append(key)
    return hashtable

def histogram_equilized(keys, L):
    """ Apply histogram equilization to the distribution of keys
    Args:
        keys: [string]
        L: int
    Returns:
        string -> int
    """
    hist = Counter(keys)
    labels, freqs = zip(*hist.items())
    cdf = dict(zip(labels, numpy.cumsum(freqs)))

    cdf_min = freqs[0]
    MN = len(keys)
    return lambda v: int(round((cdf[v] - cdf_min) / (MN - cdf_min) * (L - 1)))

def collision_stat(hashtable):
    """ Statstic the (average, standard deviation) of collisions in hashtable
    Args:
        hashtable: {int: [string]}
    Returns:
        (int, int)
    """
    collision = [len(bucket) for bucket in hashtable]
    return (numpy.mean(collision), numpy.std(collision))


if __name__ == '__main__':
    import sys
    import json
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:")
        opts = dict(opts)
    except getopt.GetoptError:
        print('\nInvalid options')
        sys.exit(1)

    size = int(opts['-s']) if '-s' in opts else 256
    with open(args[0]) as readfile:
        lines = readfile.readlines()

    h = histogram_equilized([line[0:6] for line in lines], size)
    tokens = [sID_HE(line, h) for line in lines]

    result = generate_hashtable(tokens, xor8, size)
    print(json.dumps(result, indent=4))
