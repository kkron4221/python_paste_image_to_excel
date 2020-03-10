import cv2

filename = "1-1-1.png"
imgCV = cv2.imread(filename)
imgCV_width = imgCV.shape[1]
resize_img = cv2.resize(imgCV, (imgCV_width, 700), interpolation = cv2.INTER_CUBIC)
cv2.imshow("image", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()