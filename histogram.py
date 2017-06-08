#! /usr/bin/python3
import matplotlib.pyplot as plot

def show_histogram(stat, length=20):
    y_max = max(max(stat), length)
    for x, y in enumerate(stat):
        y_len = int(length * y / y_max)
        print('{:>3}: {}'.format(x, '*' * y_len))
    print('\nmax: {}, min: {}, avg: {:.2f}' \
          .format(max(stat), min(stat), sum(stat) / len(stat)))

def show_histogram_gui(stat):
    plot.hist(stat, bins=range(min(stat), max(stat)))
    plot.show()


if __name__ == '__main__':
    import sys
    import json
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "g", [])
        options = dict(opts)
    except getopt.GetoptError:
        print('Invalid options')
        sys.exit(1)

    result = json.load(sys.stdin)
    height = [len(bucket) for bucket in result]

    if '-g' in options:
        show_histogram_gui(height)
    else:
        show_histogram(height)
