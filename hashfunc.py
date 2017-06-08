#! /usr/bin/python3
from functools import reduce

djb2 = lambda bytelist: reduce(lambda prev, curr: (prev * 33 + curr) % (2 ** 32), bytelist, 5381)

if __name__ == '__main__':
    import sys
    import json
    import getopt
    import fileinput

    try:
        opts, args = getopt.getopt(sys.argv[1:], "b:", [])
        options = dict(opts)
    except getopt.GetoptError:
        print('Invalid options')
        sys.exit(1)

    buckets = int(options['-b']) if '-b' in options else 10

    result = [[] for _ in range(buckets)]
    for line in fileinput.input():
        byte = bytes(line, 'utf-8')
        result[djb2(byte) % buckets].append(line)
    print(json.dumps(result))
