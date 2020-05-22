import cv2 as cv

img = cv.imread('../Input_Image/Shadow_Paper.jpg', 0)
img = cv.resize(img, (500, 600))

# Dilating to get rid of Text
dilated = cv.dilate(img,kernel=(1,1),iterations=1)

# blur1 = cv.GaussianBlur(dilated,(5,5),0)
blur2 = cv.medianBlur(img,21)
# diff1 = 255 - cv.absdiff(img,blur1)

# gives 0 for white areas(ie |255-255|=|0|) & 255 for Black areas(ie |0-255|=|255|).
# As we have received opposite results we inverse it for desired output.
diff2 = 255 - cv.absdiff(img,blur2)

# Normalize for full dynamic range
norm_img = diff2.copy()
cv.normalize(diff2,norm_img,alpha=0,beta=255,norm_type=cv.NORM_MINMAX)

# At this point we still have the paper somewhat gray. We can truncate that away, and re-normalize the image.
ret, thresh = cv.threshold(norm_img,230,0,cv.THRESH_TRUNC)
cv.normalize(thresh,thresh,alpha=0,beta=255,norm_type=cv.NORM_MINMAX)

# cv.imshow('show1',diff1)
cv.imshow('show2',thresh)
cv.waitKey(0)
cv.destroyAllWindows()