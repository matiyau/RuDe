def matrixForm(Arduino) :
    from picamera import PiCamera
    from time import sleep
    import cubeRot
    import numpy as np
    import math
    import cv2
    import serial

    camera = PiCamera()
    camera.resolution = (320,320)
    cube_sides = ['Front', 'Left', 'Back', 'Right', 'Up', 'Down']
    side='temp'
    mat=[[[[5 for plane in range(0,3)] for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    
    def col_feed(col_hsv_pdn) :
        print col_hsv_pdn[0], "  ", col_hsv_pdn[1], "  ", col_hsv_pdn[2],
        if (col_hsv_pdn[0]>75 and col_hsv_pdn[0]<=180) and (col_hsv_pdn[1]>=80) :
            print ' Green'
            return 1
        elif (col_hsv_pdn[0]>186 and col_hsv_pdn[0]<260) and (col_hsv_pdn[1]>=45) :
            print ' Blue'
            return 2
        elif (col_hsv_pdn[0]>337 or col_hsv_pdn[0]<7) and (col_hsv_pdn[1]>=30) :
            print ' Red'
            return 0
        elif (col_hsv_pdn[0]>7 and col_hsv_pdn[0]<35) and (col_hsv_pdn[1]>=55 and col_hsv_pdn[1]<90) :
            print ' Orange'
            return 5
        elif ((col_hsv_pdn[0]>18 and col_hsv_pdn[0]<55) and (col_hsv_pdn[1]>90)) or ((col_hsv_pdn[0]>=55 and col_hsv_pdn[0]<65) and (col_hsv_pdn[1]>80)) :
            print ' Yellow'
            return 3
        else :
            print ' White'
            return 4
    
    def capt_proc (side) :
        camera.capture(side + '_raw.jpg')
        image=cv2.imread(side + '_raw.jpg')
        b_ave=[float(0), float(0), float(0), float(0)]
        g_ave=[float(0), float(0), float(0), float(0)]
        r_ave=[float(0), float(0), float(0), float(0)]

        for x in range(80,120) :
            for y in range(80,120) :
                b_ave[1]= b_ave[1] + (float(image[x, y, 0])/1600)
                g_ave[1]= g_ave[1] + (float(image[x, y, 1])/1600)
                r_ave[1]= r_ave[1] + (float(image[x, y, 2])/1600)

        for x in range(200,240) :
            for y in range(80,120) :
                b_ave[0]= b_ave[0] + (float(image[x, y, 0])/1600)
                g_ave[0]= g_ave[0] + (float(image[x, y, 1])/1600)
                r_ave[0]= r_ave[0] + (float(image[x, y, 2])/1600)

        for x in range(80,120) :
            for y in range(200,240) :
                b_ave[3]= b_ave[3] + (float(image[x, y, 0])/1600)
                g_ave[3]= g_ave[3] + (float(image[x, y, 1])/1600)
                r_ave[3]= r_ave[3] + (float(image[x, y, 2])/1600)
                
        for x in range(200,240) :
            for y in range(200,240) :
                b_ave[2]= b_ave[2] + (float(image[x, y, 0])/1600)
                g_ave[2]= g_ave[2] + (float(image[x, y, 1])/1600)
                r_ave[2]= r_ave[2] + (float(image[x, y, 2])/1600)

        image=cv2.resize(image, (80,80), interpolation=cv2.INTER_CUBIC)
        for x in range(0,40) :
            for y in range(0,40) :
                image[x, y] =  [b_ave[0], g_ave[0], r_ave[0]]

        for x in range(40,80) :
            for y in range(0,40) :
                image[x, y] =  [b_ave[1], g_ave[1], r_ave[1]]

        for x in range(0,40) :
            for y in range(40,80) :
                image[x, y] =  [b_ave[2], g_ave[2], r_ave[2]]

        for x in range(40,80) :
            for y in range(40,80) :
                image[x, y] =  [b_ave[3], g_ave[3], r_ave[3]]

        cv2.imwrite(side + '_prcsd.jpg', image)
         
        for i in range(0,4):
            col_hsv_cv=cv2.cvtColor(np.uint8([[[b_ave[i], g_ave[i], r_ave[i]]]]), cv2.COLOR_BGR2HSV)
            col_hsv_pdn=[2*col_hsv_cv[0][0][0], float(col_hsv_cv[0][0][1])/255*100, float(col_hsv_cv[0][0][2])/255*100]
            mat[i/2][i%2][1][0] = col_feed(col_hsv_pdn)
            

    for side in cube_sides :
        print side
        for cntdwn in range(5,0,-1) :
            #print cntdwn
            sleep(1)
        capt_proc(side)
        #print mat[0][1][1][0], '  ', mat[1][1][1][0]
        #print mat[0][0][1][0], '  ', mat[1][0][1][0], '\n'
        if side != 'Up' and side != 'Down':
            cubeRot.full('up', 1, mat)
        elif side = 'Up' :
            cubeRot.full('left', 1, mat)
            cubeRot.full('left', 1, mat)
        else
            cubeRot.full('left', -1, mat)
        if side == 'Right':
            cubeRot.full('left', -1, mat)       
        #print mat[0][0][0][2], '  ', mat[0][0][1][2]
        #print mat[1][0][0][2], '  ', mat[1][0][1][2], '\n'

    return mat
