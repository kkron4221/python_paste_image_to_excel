import cv2

filename = "1-1-1.png"
imgCV = cv2.imread(filename) 
cv2.imshow("image", imgCV)
cv2.waitKey(0)
cv2.destroyAllWindows()