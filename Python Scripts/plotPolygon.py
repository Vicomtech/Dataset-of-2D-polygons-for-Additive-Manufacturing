from matplotlib import pyplot as plt
import numpy as np

def plotPolygon(polygon):
    for p in range(len(polygon)):
        for i in range(len(polygon[p])):
            np.asarray(polygon[p][i])
            for k in range(len(polygon[p][i])):
                np.asarray(polygon[p][i][k])
                polygon_x = []
                polygon_y = []
                for j in range(len(polygon[p][i][k])):
                    plt.plot([polygon[p][i][k][j - 1][0], polygon[p][i][k][j][0]], [polygon[p][i][k][j - 1][1], polygon[p][i][k][j][1]], 'k', linewidth = 2)
                    polygon_x.append(polygon[p][i][k][j - 1][0])
                    polygon_y.append(polygon[p][i][k][j - 1][1])

                if k == 0:
                    plt.fill(polygon_x, polygon_y, 'silver')
                else:
                    plt.fill(polygon_x, polygon_y, 'w')
                plt.axis('equal')