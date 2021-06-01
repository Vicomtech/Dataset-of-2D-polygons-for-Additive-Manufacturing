#!/usr/bin/env python3

from plotInfill import plotInfill
from plotInfill import plotInfillSegment2Segment
from plotPolygon import plotPolygon
from loadPolygon import loadPolygon
from loadTxt import loadInfillTxt

import sys
from matplotlib import pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) not in [3, 4] or not sys.argv[1].lower().endswith(".json") or not sys.argv[2].lower().endswith(".txt"):
        sys.exit("Usage: " + sys.argv[0] + " <polygon-file.json> <infill-file.txt> <index-of-infill-to-plot>")

    # Load polygon
    polygon = loadPolygon(sys.argv[1])

    # Load infills
    infills = loadInfillTxt(sys.argv[2])

    if len(sys.argv) != 4:
        indices = [i for i in range(len(infills))]
    else:
        indices = [int(sys.argv[3])]
    if any(i < 0 or i >= len(infills) for i in indices):
        sys.exit("Index out of range, the index must go from 0 to " + str(len(infills) - 1))

    for i in indices:
        plotPolygon(polygon)

        # Plot the final path
        plotInfill(infills[i])

        # Plot the final path segment by segment
        # plotInfillSegment2Segment(infills[i])
        plt.show()
