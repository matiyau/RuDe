def matrixForm(Arduino) :
    #from picamera import PiCamera
    import pickle
    from time import sleep
    from math import cos, radians, sqrt
    import cubeRot
    import cv2
    #import serial

    #camera = PiCamera()
    #camera.resolution = (320,320)
    cube_sides = ['Front', 'Left', 'Back', 'Right', 'Up', 'Down']
    side='temp'
    opp=[-1 for x in range (0,6)]
    mat=[[[[-1 for plane in range(0,3)] for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    cor=[[[-1 for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]
    sort=[[[[[0 for hs in range (0,3)] for plane in range(0,3)] for z in range (0,2)] for y in range (0,2)] for x in range (0,2)]

    '''
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
    '''
    
    # Capture and process the images of each side side to extract the Hue-Saturation values
    def capt_proc (side) :
        #camera.capture(side + '_raw.jpg')
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

        '''
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
        '''
         
        for i in range(0,4):
            #col_hsv_cv=cv2.cvtColor(np.uint8([[[b_ave[i], g_ave[i], r_ave[i]]]]), cv2.COLOR_BGR2HSV)
            #sort[i/2][i%2][1][0] = np.array(col_hsv_cv[0][0][0:2]).tolist()
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
        '''r1=float(p1[1])
        r2=float(p2[1])
        a1=float(p1[0])
        a2=float(p2[0])
        d=((r1*r1)+(r2*r2)-(2*r1*r2*cos(radians(a1-a2))))'''
        d=sqrt(float(p1[0]-p2[0])**2 + float(p1[1]-p2[1])**2 + float(p1[2]-p2[2])**2) 
        #print d
        return d
        #return ((r1*r1)+(r2*r2)-(2*r1*r2*cos(radians(a1-a2))))
    
    
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
        #for cntdwn in range(5,0,-1) :
            #print cntdwn
            #sleep(1)
        capt_proc(side)
        #print mat[0][1][1][0], '  ', mat[1][1][1][0]
        #print mat[0][0][1][0], '  ', mat[1][0][1][0], '\n'
        if side != 'Up' and side != 'Down':
            cubeRot.full('up', 1, mat)
            cubeRot.full('up', 1, sort)
        elif side == 'Up' :
            cubeRot.full('left', 1, mat)
            cubeRot.full('left', 1, mat)
            cubeRot.full('left', 1, sort)
            cubeRot.full('left', 1, sort)
        else:
            cubeRot.full('left', -1, mat)
            cubeRot.full('left', -1, sort)
        if side == 'Right':
            cubeRot.full('left', -1, mat)
            cubeRot.full('left', -1, sort)
        #print mat[0][0][0][2], '  ', mat[0][0][1][2]
        #print mat[1][0][0][2], '  ', mat[1][0][1][2], '\n'
        print "Next\n"


    print sort

    # Group 5 colours of the cube
    for i in range (0,5) :
        for j in range (0,24):
            if m(j)!=(-1):
                continue
            group(j,i)
            break


    # Assign the last colour to the remaining 4 colours
    for i in range (0,24):
        if m(i)==(-1):
            asgn(i, 5)

    for i in range (0,24):
        print m(i)
        if i%3==2:
            print "\n"

    pair()
    #print opp
    #print mat
        
    for i in range (0,24):
        if m(i)==opp[0] :
            asgn(i, 5)
        elif m(i)==opp[1] :
            asgn(i, 4)
        elif m(i)==opp[2] :
            asgn(i, 3)

    pair()

    '''
    for x in range(0,2):
        for y in range (0,2) :
            for z in range (0,2):
                add = mat[x][y][z][0] + mat[x][y][z][1] + mat[x][y][z][2] - 3
                cor[x][y][z]=(add/5)+(((add%5)**3 + 17*(add%5))/6 - (add%5)**2)
    '''               
    #print cor
    print mat

    with open('Matrix', 'wb') as comb:
        pickle.dump(mat, comb)
'''
    with open('Corner', 'wb') as corner:
        pickle.dump(cor, corner)
'''


#matrixForm(3)
