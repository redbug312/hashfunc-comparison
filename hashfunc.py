#! /usr/bin/python3
""" Hash every inputs to generate a hashtable
"""

from operator import add, xor
from functools import reduce
import numpy

# hash functions: bytes -> int
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
        hashtable: [[string]]
    """
    hashtable = [[] for _ in range(bucket)]
    for key in keys:
        index = hashfunc(key) % bucket
        hashtable[index].append(key)
    return hashtable

# def histogram_equilization(hashtable, bins):

def collision_stat(hashtable):
    """ Statstic the (average, standard deviation) of collisions in hashtable
    Args:
        hashtable: {int: [string]}
    Returns:
        stat: (int, int)
    """
    collision = [len(bucket) for bucket in hashtable]
    return (numpy.mean(collision), numpy.std(collision))


if __name__ == '__main__':
    import sys
    import json
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:f:")
        options = dict(opts)
    except getopt.GetoptError:
        print('Invalid options')
        sys.exit(1)

    filename = options['-f']
    size = int(options['-s']) if '-s' in options else 1600

    with open(filename) as f:
        lines = [bytes(line.strip(), 'utf-8') for line in f.readlines()]
        # lines = [[int(line[0:3]), int(line[3:6]), int(line[6:9])] for line in f.readlines()]
        # lines = [list(map(int, line.strip().split())) for line in f.readlines()]

    result = generate_hashtable(lines, xor8, size)
    print(json.dumps(result, indent=4))
