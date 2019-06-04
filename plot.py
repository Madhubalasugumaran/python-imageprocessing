import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]
img1_name = 'data.png'
img1 = cv.imread(img1_name)

px = img1[100,100]

print (px)

img2_name = 'aa.png'

img2 = cv.imread(img2_name)

px1 = img2[100,100]

print (px1)

if px1[0] >= 230:
   print ("")
   if px1[1] >= 224:
      print(img2_name+" is XL File")

elif px1[0] <= 16:
   print ("")
   if px1[1] <= 24:
      print(img1_name+" is XL File")	
else:
	print("not XL file")
			
if px[0] >= 255:
   print ("")
   if px[1] >= 255:
      print(img1_name+" is Word File")			
else:
	print("not word file")

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()