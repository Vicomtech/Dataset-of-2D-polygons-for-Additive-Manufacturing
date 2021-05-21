# Dataset of 2D polygons for Additive Manufacturing
The following repository is linked to the article entitled: "Generation of continuous hybrid zig-zag and contour paths for 3D printing". As described in the article, the repository contains a dataset of 15 convex polygons and 19 non-convex polygons in order to validate the methods described in the article.
If you use any of the provided material in your work, please cite us as follows:

## Repository structure
* **Polygons:** the folder contains 2 folders with the coordinates of 34 2D polygons (15 convex and 19 non-convex) in *.json* files.
	* **Convex polygons:** Folder containing the *.json* files with the coordinates of 15 convex polygons.
	* **Non-convex polygons:** Folder containing the *.json* files with the coordinates of 19 non-convex polygons.
	The structure of each *.json* file is as follows:
	```
	[{"boundary":
   [[X1, Y1],
    [X2, Y2],
    [X3, Y3],
	   .
	   .
	   .
    [Xi, Yi],
	   .
	   .
	   .
    [Xn, Yn],
  "children":
   [{"boundary":
      [[x1, y1],
       [x2, y2],
       [x3, y3],
	       .
		   .
		   
       [xi, yi],
	       .
		   .
		   .
	   [xn, yn]}]}]
	```

* **Infill paths:** the folder contains 34 *.txt. files with the coordinates of the infill paths generated for each of the polygons of this repository. The structure of each *.txt* file is the following:
	```
	Separation 1: S1, Separation 2: S2, Angle: A, Keep original separations: Yes/No
	X: X1 Y: Y1
	X: X2 Y: Y2
	X: X3 Y: Y3
	.
	.
	.
	X: Xi Y: Yi
	.
	.
	.
	X: Xn Y: Yn
	Separation 1: S1', Separation 2: S2', Angle: A', Keep original separations: Yes/No
	X: X1' Y: Y1'
	X: X2' Y: Y2'
	X: X3' Y: Y3'
	.
	.
	.
	X: Xi' Y: Yi'
	.
	.
	.
	X: Xn' Y: Yn'
	.
	.
	.
	```
	If Keep original separations is Yes, the chosen separations remain fix, while if it is No, the separations were automatically adjusted to ensure that all the convex (sub)polygon was completely filled.
* **Python Scripts:** the folder contains 5 *.py* scripts to plot the polygons and the generated infills.
	* *loadPolygon.py:* this script has the functions needed to load the polygon and split it into polygons of maximum depth 2.
	* *loadTxt.py:* this script has the functions needed to load the infills generated for a polygon.
	* *plotPolygon.py:* this script has the functions needed to plot the polygon.
	* *plotInfill.py:* this script has the functions needed to plot the infill generated for a polygon.
	* *main.py:* this script plots a polygon and all the infills generated for it.