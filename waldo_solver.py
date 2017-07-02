# Uses template matching 
# later: haar cascades, classifier
import cv2
import numpy as np
from matplotlib import pyplot


# go through all pics in folder
# except do it later
# for now just do 1 pic

problem_img = cv2.imread('waldo1.png')
template_img = cv2.imread('template.png')



#'cv2.TM_CCOEFF', 
#'cv2.TM_CCOEFF_NORMED'
#'cv2.TM_CCORR',
# 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

res = cv2.matchTemplate(problem_img, template_img, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print tuple(template_img.shape[1::-1])

x = max_loc[0]
y = max_loc[1]


mask = np.zeros(problem_img.shape, dtype = "uint8")
solved = cv2.addWeighted(problem_img, 0.25, mask, 0.75, 0)

# cropped = problem_img[0:y+206, 0:x+86]

# cv2.rectangle(problem_img, (x, y), (x+10, y+10), 2, 255)
cv2.putText(problem_img, "HELLO", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)

cv2.imwrite('solved.png', problem_img)

cv2.imshow("no", problem_img)
cv2.waitKey(0)

