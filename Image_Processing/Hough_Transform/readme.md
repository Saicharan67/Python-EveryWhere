# HOUGH TRANSFORM
The Hough transform can be used to detect lines, circles or other parametric curves. Hough transform can detect lines, circles and other structures if their parametric equation is known.
The basic idea here is a straight line y=mx+b can be represented as a point (m,b) in parameter space.

### STEPS:
• Edge detection, using the Canny edge detector

• Mapping of edge points to the Hough space and storage in an accumulator

• Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding.

• Conversion of infinite lines to finite lines.

Results:

### Lane detection:
##### Input image
<img src="https://github.com/amoghatsunil/Python-EveryWhere/blob/master/Image_Processing/Hough_Transform/images/road.jfif">

##### Output image
<img src="https://github.com/amoghatsunil/Python-EveryWhere/blob/master/Image_Processing/Hough_Transform/images/line_Detected.png">
