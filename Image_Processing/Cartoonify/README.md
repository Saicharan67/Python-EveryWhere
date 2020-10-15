
CARTOONIFY AN IMAGE USING OPEN CV
==========================================================================

#### Steps to follow :

First we need to load an image and converting into grayscale image for easy processing.
We will blur the image so we can reduce the noise.
We then apply a bilateral filter to reduce the color palette of the image.
Then we will create an edge mask from gray scale image using adaptive threshold.
Finally combine the color image with edge mask produced.

### Input :

[Images/building.jpg]


### Output:

[Images/CartoonImage.png]