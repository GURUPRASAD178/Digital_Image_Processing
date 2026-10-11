import cv2
import numpy as np

img = cv2.imread("sample.jpg")
img = cv2.resize(img,(400,400))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_NONE)

cnt=max(contours,key=cv2.contourArea)

direction={
    (1,0):0,
    (1,-1):1,
    (0,-1):2,
    (-1,-1):3,
    (-1,0):4,
    (-1,1):5,
    (0,1):6,
    (1,1):7
}

chain=[]

points=cnt.squeeze()

for i in range(len(points)-1):

    x1,y1=points[i]

    x2,y2=points[i+1]

    dx=np.sign(x2-x1)

    dy=np.sign(y2-y1)

    chain.append(direction.get((dx,dy),-1))

output=img.copy()

cv2.drawContours(output,[cnt],-1,(0,255,0),2)

print("Freeman Chain Code")

print(chain)

cv2.imshow("Chain Code",output)

cv2.waitKey(0)

cv2.destroyAllWindows()



import cv2
import numpy as np

img=cv2.imread("sample.jpg",0)

img=cv2.resize(img,(400,400))

_,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

element=cv2.getStructuringElement(
        cv2.MORPH_CROSS,
        (3,3))

skeleton=np.zeros(img.shape,np.uint8)

while True:

    eroded=cv2.erode(img,element)

    temp=cv2.dilate(eroded,element)

    temp=cv2.subtract(img,temp)

    skeleton=cv2.bitwise_or(skeleton,temp)

    img=eroded.copy()

    if cv2.countNonZero(img)==0:

        break

cv2.imshow("Skeleton",skeleton)

cv2.waitKey(0)

cv2.destroyAllWindows()




import cv2

img=cv2.imread("sample.jpg")

img=cv2.resize(img,(400,400))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(th,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

cnt=max(contours,key=cv2.contourArea)

epsilon=0.02*cv2.arcLength(cnt,True)

approx=cv2.approxPolyDP(cnt,
                        epsilon,
                        True)

output=img.copy()

cv2.drawContours(output,
                 [approx],
                 -1,
                 (0,255,0),
                 3)

print("Number of Vertices =",len(approx))

cv2.imshow("Polygon Approximation",output)

cv2.waitKey(0)

cv2.destroyAllWindows()