import numpy as haha
import cv2
poo = cv2.imread("E:/f.jpg")
b,g,r = cv2.split(poo)
bn = haha.zeros(b.shape)
gn = haha.zeros(g.shape)
rn = haha.zeros(r.shape)
bi = cv2.imwrite('E:/b.jpg',b)
gi = cv2.imwrite('E:/g.jpg',g)
ri = cv2.imwrite('E:/r.jpg',r)
bb = cv2.merge((b,g,r))
bbmerge = cv2.imwrite('E:/merged.jpg', bb)
#cv2.namedWindow('f',cv2.WINDOW_FREERATIO)

