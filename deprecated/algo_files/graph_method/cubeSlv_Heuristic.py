def steps () :
    import corRot as cR
    from copy import deepcopy as cp
    from math import factorial as fact

    #Set the principle corner positions
    corn=[[[0,1],[2,3]],[[4,5],[6,7]]]

    #List Of Various Goal Positions Possible
    goal=[corn for i in range (0,24)]

    #List of coordinates of each corner in one permutation
    prob=[[-1 for i in range(0,3)] for j in range(0,8)]

    #List of coordinates of each corner in all possible orientations of the solved cube
    coord=[[[-1 for i in range (0,3)] for j in range (0,8)] for k in range (0,24)]

    #List of corners available at each position
    perm=[[i for i in range (0,8)] for j in range (0,8)]

    #List of manhattan distances for all permutations of corners
    manh=[-1 for i in range (0,fact(8))]

    #Calculate the manhattan distance between the current state and the solved state
    def man_dist(cur, target):
        #Set distance to maximum value possible
        #This is when all corners are opposite to required positions
        dist=48
        #print cur
        #print target
        for i in range (0,24) :
            temp=0
            for j in range (0,8):
                temp=temp+abs(cur[j][0]-target[i][j][0])+abs(cur[j][1]-target[i][j][1])+abs(cur[j][2]-target[i][j][2])
            if dist>temp:
                dist=temp
        return float(dist)/4
    
    #Calculate the permutation from its index number
    def calc_index2perm(pos, i, j):
        temp=cp(pos)
        cor=temp[7-j][i/fact(j)]
        prob[cor]=[((7-j)/4)%2, ((7-j)/2)%2, (7-j)%2]
        if j==0:
            return
        for k in range(8-j, 8):
            temp[k].remove(cor)
        calc_index2perm(temp, i%fact(j), j-1)
        if j==7:
            return prob
        return
    

    for i in range (0,4) :        
        for j in range (0,4) :
            goal[4*i+j]=cp(corn)
            cR.full('front', 1, corn)            
        cR.full('up', 1, corn)

    cR.full('left', 1, corn)
    for j in range (0,4) :
        goal[16+j]=cp(corn)
        cR.full('front', 1, corn)

    cR.full('left', 2, corn)
    for j in range (0,4) :
        goal[20+j]=cp(corn)
        cR.full('front', 1, corn)
        
    cR.full('left', 1, corn)

    for i in range (0,24) :
        for x in range (0,2) :
            for y in range (0,2) :
                for z in range (0,2) :
                    coord[i][goal[i][x][y][z]]=[x,y,z]

    for i in range (0,fact(8)) :
       manh[i]=man_dist(calc_index2perm(perm, i, 7), coord)
       #print i, manh[i]

    print manh


steps()
    
        
        
