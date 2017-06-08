#! /usr/bin/python3
import matplotlib.pyplot as plot

def show_histogram(stat):
    print('Not implemented yet, turned to pyplot ver.')
    show_histogram_gui(stat)

def show_histogram_gui(stat):
    plot.hist(stat)
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
