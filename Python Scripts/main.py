from plotInfill import plotInfill
from plotPolygon import plotPolygon
from loadPolygon import loadPolygon
from loadTxt import loadInfillTxt

import json
from matplotlib import pyplot as plt

# Load polygon
polygon = loadPolygon('square_grandchildren.json')

# Load infills
infills = loadInfillTxt("square_grandchildren.txt")

# Plot infills and polygons
for i in range(len(infills)):
    plotPolygon(polygon)
    plotInfill(infills[i])
    plt.show()


