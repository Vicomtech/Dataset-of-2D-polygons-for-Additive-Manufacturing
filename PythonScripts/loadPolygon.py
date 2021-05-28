import json

def splitTree(aux_polygon, tree, depth, pos):
    "It reorganizes the original polygon hierarchy, obtaining a tree of maximum depth 2"
    if 'boundary' in aux_polygon.keys():
        if depth % 2 == 0:
            tree.append([aux_polygon['boundary']])
    if 'children' in aux_polygon.keys():
        depth = depth + 1
        aux_polygon = aux_polygon['children']
        if depth % 2 == 1:
            for i in range(len(aux_polygon)):
                tree[pos].append(aux_polygon[i]['boundary'])
            pos = pos + 1
        for i in range(len(aux_polygon)):
            splitTree(aux_polygon[i], tree, depth, pos)

    return(tree)

def loadPolygon(polygonJson):
    # Load .json file
    with open(polygonJson) as json_file:
        loadedPolygon = json.load(json_file)

    # Split polygon tree in polygons of maximum depth 2
    polygon = []
    depth = 0
    pos = 0
    for i in range(len(loadedPolygon)):
        top_level = []
        aux_polygon = loadedPolygon[i]
        polygonDepth2 = splitTree(aux_polygon, top_level, depth, pos)
        polygon.append(polygonDepth2)

    return (polygon)

