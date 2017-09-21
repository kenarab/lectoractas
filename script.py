import sys
import ipdb
import numpy as np
import cv2
from matplotlib import pyplot as plt


filename = sys.argv[1]
gray = cv2.imread(filename)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imwrite(filename.replace(".jpeg", "-edges.jpg"), edges)
minLineLength = 100
hlines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=250, lines=np.array([]),
                         minLineLength=minLineLength, maxLineGap=80)



def onclick(event):
    global selected_point
    selected_point = (event.x, event.y)
    print('button=%d, x=%d, y=%d, xdata=%s, ydata=%s' %
                       (event.button, event.x, event.y, event.xdata, event.ydata))


a, b, c = hlines.shape

lines = [((hlines[0][i][0], hlines[0][i][1]), (hlines[0][i][2], hlines[0][i][3])) for i in range(b)]

for l in lines:
    cv2.line(gray, l[0], l[1], (0, 0, 255), 1, cv2.CV_AA)

cv2.imwrite(filename.replace(".jpeg", "-houghlines.jpg"), gray)

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
figure = plt.figure()
mplib_img = plt.imshow(gray, cmap='gray', interpolation='bicubic')
figure.images.append(mplib_img)

figure.canvas.mpl_connect('button_press_event', onclick)

plt.show()
ipdb.set_trace()

# La idea de este script era probar el reconocimiento de las líneas y en principio permitir al usuario
# seleccionar una celda. Luego debería recortarse esa celda (contenida por el cruce las líneas horizontales y
# verticales más cercanas) y sobre ella aplicar detección de contornos y hacer los pasos siguientes. Es
# simplemente un comienzo para resolver los pasos del 1, 3, 4 y 5 del README.
