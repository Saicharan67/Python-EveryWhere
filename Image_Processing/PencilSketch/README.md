

PENCIL SKETCH OF AN IMAGE USING OPENCV
===========================================================

An image is basically an array of numbers to Python.So we can perform a variety of matrix manipulation to get some interesting results.The steps to reduce an image into 'pencil outline' are:

1.IMPORTING LIBRARIES

2.LOADING AN IMAGE

3.CONVERTING AN IMAGE INTO GRAYSCALE

Converting an image into grayscale gives us black & white pixels in the image which is used for creating a pencil sketch. 

4.INVERTING AN IMAGE

We are using the bitwise_not function which is used to make brighter regions lighter and vice versa so that we can find the edges to create a pencil sketch. 

5.SMOOTHING THE IMAGE

We have used the gaussian blur technique with 21 x 21 pixel and the default sigma values filter on the image to smoothen our image. By increasing the filter size, we can create thin lines for our sketch and it is used to reduce the noise in the image. 

6.OBTAINING THE OUTPUT

Dividing the greyscale value of the image by the inverse of blurred image value which highlights the boldest edges. This technique is used by traditional photographers to print photos from the reel.

          Then we got the output by using opencv 
