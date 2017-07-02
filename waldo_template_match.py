import cv2
import numpy as np

print 'starting'

problem_img = cv2.imread('waldo1.png')
problem_img = cv2.cvtColor(problem_img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.png', 0)

w, h = template.shape[::-1]

result = cv2.matchTemplate(problem_img, template, cv2.TM_CCOEFF)
threshold = 0.8

location = np.where(result >= threshold)

print 'problem_img'

for pt in zip(*location[::-1]):
	cv2.rectangle(template, pt, (pt[0] + w, pt[1] + h), (0,255,255), 5)
	print 'had'

cv2.imshow('Solved', problem_img)
cv2.waitKey(0)

print ' dont'