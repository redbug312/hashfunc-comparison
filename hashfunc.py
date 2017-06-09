#! /usr/bin/python3
""" Hash every inputs to generate a hashtable
"""

from functools import reduce

# hash functions: bytes -> int
djb2 = lambda bytes_: reduce(lambda prev, curr: (prev * 33 + curr) % (2 ** 32), bytes_, 5381)

def generate_hashtable(keys, hashfunc, bucket):
    """ Generate the hashtable from given arguments
    Args:
        keys: string
        hashfunc: bytes -> int
        bucket: int
    Returns:
        hashtable: [[string]]
    """
    hashtable = [[] for _ in range(bucket)]
    for key in keys:
        byte = bytes(key.strip(), 'utf-8')
        index = hashfunc(byte) % bucket
        hashtable[index].append(key)
    return hashtable

def collision_stat(hashtable):
    """ Statstic the (max, min, sum, mean) of collisions in hashtable
    Args:
        hashtable: {int: [string]}
    Returns:
        stat: (int)
    """
    return [len(bucket) for bucket in hashtable.values()]


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
        lines = f.readlines()

    result = generate_hashtable(lines, djb2, size)
    print(json.dumps(result, indent=4))
