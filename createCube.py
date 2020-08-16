import cv2
import numpy as np

front = np.zeros((320,320,3), np.uint8)
back = np.zeros((320,320,3), np.uint8)

up = np.zeros((320,320,3), np.uint8)
down = np.zeros((320,320,3), np.uint8)

left = np.zeros((320,320,3), np.uint8)
right = np.zeros((320,320,3), np.uint8)

col_rgb = [[0,0,255],[0,89,255],[0,255,0],[255,0,0],[0,229,255],[255,255,255]]
col_code = ['r', 'o', 'g', 'b', 'y', 'w']

print "Enter Corner Colours [Front/Back] [Left/Right] [Up/Down]\n"

ulb = raw_input("ULB : ")

index = col_code.index(ulb[0])
for y in range(160,320) :
    for x in range(0,160) :
        back[x,y,0] = col_rgb[index][0]
        back[x,y,1] = col_rgb[index][1]
        back[x,y,2] = col_rgb[index][2]

index = col_code.index(ulb[1])
for y in range(0,160) :
    for x in range(0,160) :
        left[x,y,0] = col_rgb[index][0]
        left[x,y,1] = col_rgb[index][1]
        left[x,y,2] = col_rgb[index][2]

index = col_code.index(ulb[2])
for y in range(0,160) :
    for x in range(0,160) :
        up[x,y,0] = col_rgb[index][0]
        up[x,y,1] = col_rgb[index][1]
        up[x,y,2] = col_rgb[index][2]



urb = raw_input("URB : ")

index = col_code.index(urb[0])
for y in range(0,160) :
    for x in range(0,160) :
        back[x,y,0] = col_rgb[index][0]
        back[x,y,1] = col_rgb[index][1]
        back[x,y,2] = col_rgb[index][2]

index = col_code.index(urb[1])
for y in range(160,320) :
    for x in range(0,160) :
        right[x,y,0] = col_rgb[index][0]
        right[x,y,1] = col_rgb[index][1]
        right[x,y,2] = col_rgb[index][2]

index = col_code.index(urb[2])
for y in range(160,320) :
    for x in range(0,160) :
        up[x,y,0] = col_rgb[index][0]
        up[x,y,1] = col_rgb[index][1]
        up[x,y,2] = col_rgb[index][2]



ulf = raw_input("ULF : ")

index = col_code.index(ulf[0])
for y in range(0,160) :
    for x in range(0,160) :
        front[x,y,0] = col_rgb[index][0]
        front[x,y,1] = col_rgb[index][1]
        front[x,y,2] = col_rgb[index][2]

index = col_code.index(ulf[1])
for y in range(160,320) :
    for x in range(0,160) :
        left[x,y,0] = col_rgb[index][0]
        left[x,y,1] = col_rgb[index][1]
        left[x,y,2] = col_rgb[index][2]

index = col_code.index(ulf[2])
for y in range(0,160) :
    for x in range(160,320) :
        up[x,y,0] = col_rgb[index][0]
        up[x,y,1] = col_rgb[index][1]
        up[x,y,2] = col_rgb[index][2]



urf = raw_input("URF : ")

index = col_code.index(urf[0])
for y in range(160,320) :
    for x in range(0,160) :
        front[x,y,0] = col_rgb[index][0]
        front[x,y,1] = col_rgb[index][1]
        front[x,y,2] = col_rgb[index][2]

index = col_code.index(urf[1])
for y in range(0,160) :
    for x in range(0,160) :
        right[x,y,0] = col_rgb[index][0]
        right[x,y,1] = col_rgb[index][1]
        right[x,y,2] = col_rgb[index][2]

index = col_code.index(urf[2])
for y in range(160,320) :
    for x in range(160,320) :
        up[x,y,0] = col_rgb[index][0]
        up[x,y,1] = col_rgb[index][1]
        up[x,y,2] = col_rgb[index][2]



dlb = raw_input("DLB : ")

index = col_code.index(dlb[0])
for y in range(160,320) :
    for x in range(160,320) :
        back[x,y,0] = col_rgb[index][0]
        back[x,y,1] = col_rgb[index][1]
        back[x,y,2] = col_rgb[index][2]

index = col_code.index(dlb[1])
for y in range(0,160) :
    for x in range(160,320) :
        left[x,y,0] = col_rgb[index][0]
        left[x,y,1] = col_rgb[index][1]
        left[x,y,2] = col_rgb[index][2]

index = col_code.index(dlb[2])
for y in range(160,320) :
    for x in range(0,160) :
        down[x,y,0] = col_rgb[index][0]
        down[x,y,1] = col_rgb[index][1]
        down[x,y,2] = col_rgb[index][2]



drb = raw_input("DRB : ")

index = col_code.index(drb[0])
for y in range(0,160) :
    for x in range(160,320) :
        back[x,y,0] = col_rgb[index][0]
        back[x,y,1] = col_rgb[index][1]
        back[x,y,2] = col_rgb[index][2]

index = col_code.index(drb[1])
for y in range(160,320) :
    for x in range(160,320) :
        right[x,y,0] = col_rgb[index][0]
        right[x,y,1] = col_rgb[index][1]
        right[x,y,2] = col_rgb[index][2]

index = col_code.index(drb[2])
for y in range(0,160) :
    for x in range(0,160) :
        down[x,y,0] = col_rgb[index][0]
        down[x,y,1] = col_rgb[index][1]
        down[x,y,2] = col_rgb[index][2]



dlf = raw_input("DLF : ")

index = col_code.index(dlf[0])
for y in range(0,160) :
    for x in range(160,320) :
        front[x,y,0] = col_rgb[index][0]
        front[x,y,1] = col_rgb[index][1]
        front[x,y,2] = col_rgb[index][2]

index = col_code.index(dlf[1])
for y in range(160,320) :
    for x in range(160,320) :
        left[x,y,0] = col_rgb[index][0]
        left[x,y,1] = col_rgb[index][1]
        left[x,y,2] = col_rgb[index][2]

index = col_code.index(dlf[2])
for y in range(160,320) :
    for x in range(160,320) :
        down[x,y,0] = col_rgb[index][0]
        down[x,y,1] = col_rgb[index][1]
        down[x,y,2] = col_rgb[index][2]



drf = raw_input("DRF : ")

index = col_code.index(drf[0])
for y in range(160,320) :
    for x in range(160,320) :
        front[x,y,0] = col_rgb[index][0]
        front[x,y,1] = col_rgb[index][1]
        front[x,y,2] = col_rgb[index][2]

index = col_code.index(drf[1])
for y in range(0,160) :
    for x in range(160,320) :
        right[x,y,0] = col_rgb[index][0]
        right[x,y,1] = col_rgb[index][1]
        right[x,y,2] = col_rgb[index][2]

index = col_code.index(drf[2])
for y in range(0,160) :
    for x in range(160,320) :
        down[x,y,0] = col_rgb[index][0]
        down[x,y,1] = col_rgb[index][1]
        down[x,y,2] = col_rgb[index][2]


cv2.imwrite("Front_raw.jpg", front)
cv2.imwrite("Back_raw.jpg", back)
cv2.imwrite("Left_raw.jpg", left)
cv2.imwrite("Right_raw.jpg", right)
cv2.imwrite("Up_raw.jpg", up)
cv2.imwrite("Down_raw.jpg", down)
