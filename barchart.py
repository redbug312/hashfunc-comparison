#! /usr/bin/python3
def show_barchart(stat, length=20):
    y_max = max(max(stat), length)
    for x, y in enumerate(stat):
        y_len = int(length * y / y_max)
        print('{:>3}: {}'.format(x, '*' * y_len))
    print('\nmax: {}, min: {}, avg: {:.2f}' \
          .format(max(stat), min(stat), sum(stat) / len(stat)))

if __name__ == '__main__':
    import sys
    import json

    result = json.load(sys.stdin)
    collision = [len(bucket) for bucket in result]

    show_barchart(collision)
