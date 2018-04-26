from  math import sqrt
import pickle
from time import sleep
import cv2
import cubeRot
import serial
#from SimpleCV import Image, Camera


def matrixForm(Arduino) :
    cube_sides = ['Front', 'Left', 'Back', 'Right', 'Up', 'Down']
    side='temp'
    opp=[-1 for x in range (0,6)]
    mat=[[[[-1 for plane in range(0,3)] for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    cor=[[[-1 for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    sort=[[[[[0 for hs in range (0,3)] for plane in range(0,3)] for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    
    def send_Ard(k):
        Arduino.reset_input_buffer()
        Arduino.write("*<"+str(k)+"#")
        if Arduino.read(1)=='N':
            return 1
        return 0
    
    # Capture and process the images of each side side to extract the Hue-Saturation values
    def capt_proc (side) :
        camera = cv2.VideoCapture(1)
        sleep(0.5)
        camera.set(3,480)	#Height
        camera.set(4,640)	#Width

        #Discard The First Few Frames
        for i in range(0,10) :
            retval,image = camera.read()
        del(camera)
        image = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
        image = image[100:500,40:440]
        cv2.imwrite(side + '_raw.jpg',image)

        #image = cv2.imread(side + '_raw.jpg')
        b_ave=[float(0), float(0), float(0), float(0)]
        g_ave=[float(0), float(0), float(0), float(0)]
        r_ave=[float(0), float(0), float(0), float(0)]

        for x in range(0,100) :
            for y in range(0,100) :
                b_ave[1]= b_ave[1] + (float(image[x, y, 0])/10000)
                g_ave[1]= g_ave[1] + (float(image[x, y, 1])/10000)
                r_ave[1]= r_ave[1] + (float(image[x, y, 2])/10000)

        for x in range(300,400) :
            for y in range(0,100) :
                b_ave[0]= b_ave[0] + (float(image[x, y, 0])/10000)
                g_ave[0]= g_ave[0] + (float(image[x, y, 1])/10000)
                r_ave[0]= r_ave[0] + (float(image[x, y, 2])/10000)

        for x in range(0,100) :
            for y in range(300,400) :
                b_ave[3]= b_ave[3] + (float(image[x, y, 0])/10000)
                g_ave[3]= g_ave[3] + (float(image[x, y, 1])/10000)
                r_ave[3]= r_ave[3] + (float(image[x, y, 2])/10000)
                
        for x in range(300,400) :
            for y in range(300,400) :
                b_ave[2]= b_ave[2] + (float(image[x, y, 0])/10000)
                g_ave[2]= g_ave[2] + (float(image[x, y, 1])/10000)
                r_ave[2]= r_ave[2] + (float(image[x, y, 2])/10000)

        for i in range(0,4):
            sort[i/2][i%2][1][0] = [b_ave[i], g_ave[i], r_ave[i]]
            

    # Universal positioning for HUE-SATURATION value matrix
    def s(i):
        return sort[(i/12)%2][(i/6)%2][(i/3)%2][i%3]


    # Universal positioning for multidimensional colour-code matrix
    def m(i):
        return mat[(i/12)%2][(i/6)%2][(i/3)%2][i%3]


    def asgn(i,j):
        mat[(i/12)%2][(i/6)%2][(i/3)%2][i%3]=j
    

    # Find distance between two polar coordinates
    # r1, r2 are distances from origin : These are the SATURATION values
    # a1, a2 are angles made with positive X-axis : These are the HUE angles
    def dist(p1,p2):
        d=sqrt(float(p1[0]-p2[0])**2 + float(p1[1]-p2[1])**2 + float(p1[2]-p2[2])**2) 
        return d    
    
    # Group the colour at position 'i' with its 3 nearest neighbours
    # Assign the colour code 'j' to all colours in this group
    def group(i,j):
        asgn(i,j)
        for x in range (0,3):
            count=0
            for y in range (i+1,24):
                if m(y)!=(-1):
                    continue
                temp=dist(s(i), s(y))
                if count==0 :
                    dis=temp
                    pos=y
                elif dis>temp :
                    dis=temp
                    pos=y
                count=count+1
            asgn(pos,j)

    def pair():
        for col1 in range (0,3):
            for col2 in range (3,6):
                x=0
                while x<2 :
                    y=0
                    while y<2:
                        z=0
                        while z<2 :
                            if col1 in mat[x][y][z] and col2 in mat[x][y][z]:
                                break
                            z=z+1
                        if z<2 :
                            break
                        y=y+1
                    if y<2:
                        break
                    x=x+1
                if x<2:
                    continue
                opp[col1]=col2
                opp[col2]=col1
                break

    

    
    # Rotate the cube to bring each side in front of the Camera.
    for side in cube_sides :
        print side

        #Correctly Position The Cube
        #For Up, Cube is already positioned with side grippers
        if side != 'Up' :
            if send_Ard(18)==0:
                return
        
        capt_proc(side)
        if side != 'Up' and side != 'Down':
            cubeRot.full('up', 1, mat)
            cubeRot.full('up', 1, sort)
            if send_Ard(5)==0:
                return
        elif side == 'Up' :
            cubeRot.full('up', -1, mat)
            cubeRot.full('up', -1, mat)
            cubeRot.full('up', -1, sort)
            cubeRot.full('up', -1, sort)
            if send_Ard(4)==0:
                return
        else:
            cubeRot.full('up', -1, mat)
            cubeRot.full('up', -1, mat)
            cubeRot.full('up', -1, sort)
            cubeRot.full('up', -1, sort)
            if send_Ard(4)==0:
                return
            cubeRot.full('left', 1, mat)
            cubeRot.full('left', 1, sort)
            if send_Ard(0)==0:
                return
            
        if side == 'Right':
            cubeRot.full('left', -1, mat)
            cubeRot.full('left', -1, sort)
            if send_Ard(2)==0:
                return
        #print "Next\n"


    if send_Ard(18)==0:
        return
    #print sort


    # Group 5 colours of the cube
    for i in range (0,5) :
        for j in range (0,24):
            if m(j)!=(-1):
                continue
            group(j,i)
            break


    # Assign the last colour to the remaining 4 positions
    for i in range (0,24):
        if m(i)==(-1):
            asgn(i, 5)

    for i in range (0,24):
        #print m(i)
        if i%3==2:
            #print "\n"
            next

    pair()
        
    for i in range (0,24):
        if m(i)==opp[0] :
            asgn(i, 5)
        elif m(i)==opp[1] :
            asgn(i, 4)
        elif m(i)==opp[2] :
            asgn(i, 3)

    pair()
               
    #print mat

    with open('Matrix', 'wb') as comb:
        pickle.dump(mat, comb)


#matrixForm(3)
