#! /usr/bin/python3
# pylint: disable=unnecessary-lambda
import json
# import getopt
import fileinput
from collections import defaultdict
from barchart import show_barchart_gui


if __name__ == '__main__':
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], "b:", [])
    #     options = dict(opts)
    # except getopt.GetoptError:
    #     print('Invalid options')
    #     sys.exit(1)

    partA = lambda sID: sID[0:3]
    partB = lambda sID: sID[3:6]
    partC = lambda sID: sID[6:9]

    stat = defaultdict(lambda: set())
    for line in fileinput.input():
        stat[partB(line)].add(partC(line))

    result = {item: len(stat[item]) for item in stat}
    print(json.dumps(result, indent=4))
    show_barchart_gui(result, True)
