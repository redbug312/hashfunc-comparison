#! /usr/bin/python3
import matplotlib.pyplot as plot
import numpy

def show_barchart(stat, length=20):
    y_max = max(max(stat), length)
    for x, y in enumerate(stat):
        y_len = int(length * y / y_max)
        print('{:>3}: {}'.format(x, '*' * y_len))
    print('\nmax: {}, min: {}, avg: {:.2f}' \
          .format(max(stat), min(stat), sum(stat) / len(stat)))

def show_barchart_gui(stat):
    _, ax = plot.subplots()
    ax.bar(numpy.arange(len(stat)), stat)
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
        show_barchart_gui(height)
    else:
        show_barchart(height)
