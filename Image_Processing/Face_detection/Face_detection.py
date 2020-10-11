import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\admin\Pictures\harrypotter.jpg',1)
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(grayImg,scaleFactor=1.1,minNeighbors=5)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.putText(img,"Face_detected", org=(10,50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(255,0,255),thickness=2,lineType=cv2.LINE_AA)
    cv2.imshow("face_detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()