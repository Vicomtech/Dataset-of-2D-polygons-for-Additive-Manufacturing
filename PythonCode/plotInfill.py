from matplotlib import pyplot as plt

def plotInfill(infill):
    for i in range(len(infill)):
        for j in range(len(infill[i])):
            plt.plot([infill[i][j - 1][0], infill[i][j][0]], [infill[i][j - 1][1], infill[i][j][1]], 'r', linewidth = 2)
    plt.axis('equal')

def plotInfillSegment2Segment(infill):
    plt.axis('equal')
    for i in range(len(infill)):
        for j in range(len(infill[i])):
            if j == len(infill[i]) - 1:
                j = -1
            plt.plot([infill[i][j][0], infill[i][j + 1][0]], [infill[i][j][1], infill[i][j + 1][1]], 'r', linewidth = 2)
            plt.pause(0.01)
            plt.show(block=False)