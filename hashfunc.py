#! /usr/bin/python3
from functools import reduce

djb2 = lambda bytelist: reduce(lambda prev, curr: (prev * 33 + curr) % (2 ** 32), bytelist, 5381)

if __name__ == '__main__':
    import fileinput
    import json

    buckets = 90000

    result = [[] for _ in range(buckets)]
    for line in fileinput.input():
        byte = bytes(line, 'utf-8')
        result[djb2(byte) % buckets].append(line)
    print(json.dumps(result))
