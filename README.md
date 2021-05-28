# Dataset of 2D polygons for Additive Manufacturing
The following repository is linked to the article entitled: "Generation of continuous hybrid zig-zag and contour paths for 3D printing". As described in the article, the repository contains a dataset of 15 convex polygons and 19 non-convex polygons in order to validate the methods described in the article.
If you use any of the provided material in your work, please cite us as follows:

## Repository structure
* **Polygons:** the folder contains 2 folders with the coordinates of 34 2D polygons (15 convex and 19 non-convex) in *.json* files.
	* **ConvexPolygons:** Folder containing the *.json* files with the coordinates of 15 convex polygons.
	* **Non-ConvexPolygons:** Folder containing the *.json* files with the coordinates of 19 non-convex polygons.  
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
		   .
       [xi, yi],
		   .
		   .
		   .
	   [xn, yn]}]}]
	```

* **InfillPaths:** the folder contains 2 folders with some possible infills for each polygon.  
	* **ConvexPolygons:** Folder containing the *.txt* files with the infills of 15 convex polygons. 
	* **Non-ConvexPolygons:** Folder containing the *.txt* files with the infills of 19 non-convex polygons.  
	Each *.txt* file contains 48 infills for a polygon varying lines separation and orientation. The structure of the *.txt* is as follows:
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
	If Keep original separations is *Yes*, the chosen separations remain fix, while if it is *No*, the separations were automatically adjusted to ensure that all the convex (sub)polygon was completely filled.
* **PythonFiles:** the folder contains 5 *.py* files to plot the polygons and the generated infills.
	* *loadPolygon.py:* this script has the functions needed to load the polygon and split it into polygons of maximum depth 2.
	* *loadTxt.py:* this script has the functions needed to load the infills generated for a polygon.
	* *plotPolygon.py:* this script has the functions needed to plot the polygon.
	* *plotInfill.py:* this script has the functions needed to plot the infill generated for a polygon.
	* *main.py:* this script plots a polygon and all the infills generated for it.

## Polygon visualization
The code to visualize the polygons and their infills is to be executed in Python3. The inputs arguments should be:  
* 1. *main.py*
* 2. *.json* file.
* 3. *.txt* file.
* 4. (optional) the index of the infill to be plotted. In case it is empty, the 48 possible infills will be shown.

## License

## Contact
If you have any question or suggestion, do not hesitate to contact us at the following addresses:
* Gorka Gomez: ggomez@vicomtech.org
* Camilo Cortés: ccortes@vicomtech.org
* Carles Creus: ccreus@vicomtech.org
* Maialen Zelaia: mzelaia@vicomtech.org
* Aitor Moreno: amoreno@vicomtech.org
