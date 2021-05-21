import numpy as np

def loadInfillTxt(txtFile):

    # Open txt file
    infillsTxt = open(txtFile, "r")

    infillsString = infillsTxt.read().split('\n')

    INFILLS = []
    infill = []
    infills = []
    PARAMETERS = []
    for i in range(len(infillsString)):
        parameters = str()
        if infillsString[i][0] == "S":
            for j in range(len(infillsString[i])):
                parameters = parameters + infillsString[i][j]

            if (len(infill) > 0):
                infills.append(infill)
            if len(PARAMETERS) > 0:
                if parameters != PARAMETERS[len(PARAMETERS) - 1]:
                    INFILLS.append(infills)
                    infills = []
            PARAMETERS.append(parameters)
            infill = []
        else:
            x = str()
            y = str()

            # The number of X coordinate starts at position 3
            for j in np.arange(3, len(infillsString[i])):
                if (infillsString[i][j] == " "):
                    pos = j
                    break
                else:
                    x = x + infillsString[i][j]

            # The number of Y coordinate starts 4 positions after the blank space
            for j in np.arange(pos + 4, len(infillsString[i])):
                y = y + infillsString[i][j]

            infill.append([float(x), float(y)])

    return INFILLS