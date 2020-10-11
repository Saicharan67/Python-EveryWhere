



FACE DETECTION USING OPEN CV
==========================================================================

Face detection is mostly done by using haarcascade classifier.The steps to do are:

1.Importing libraries

2.Loading the image and converting it into gray scale

Input:

()[C:\Users\admin\projects\Python-EveryWhere\Image_Processing\Face_detection\Images\harrypotter.jpg]

The reason for this is gray channel is easy to process and is computationally less intensive as it contains only 1-channel of black-white.

3.Detecting features

Now we try to find the co-ordinates of face to draw a rectangle around the face and here we face_classifier,in_built function detectMultiScale, haarcascade_frontalface_default.xml.
In detectMultiScale we pass parameters:
a.GrayScale image
b.scaleFactor — Parameter specifying how much the image size is reduced
c.minNeighbors — Parameter specifying how many neighbors each candidate rectangle should have to retain it. This parameter will affect the quality of the detected faces

4.Drawing rectangle

It gives four co-ordinates x,y,width of image,height of image

5.Displaying output and text

putText takes following parameters

1.image
2.text to be displayed in string
3.fontFace:type of font style
4.org:co-ordinates to display
5.color:rgb values
6.fontScale:fontsize

Output:

()[C:\Users\admin\projects\Python-EveryWhere\Image_Processing\Face_detection\Images\Output.png]
