def steps (mat, inst, opp) :
    import cubeSfy as cS
    import cubeRot as cR
    from copy import deepcopy as cp
    
    def move(x, perm):
        if x/3==0 :
            cS.u(x%3+1, perm)
        elif x/3==1 :
            cS.d(x%3+1, perm)
        elif x/3==2 :
            cS.l(x%3+1, perm)
        elif x/3==3 :
            cS.r(x%3+1, perm)
        elif x/3==4 :
            cS.f(x%3+1, perm)
        elif x/3==5 :
            cS.b(x%3+1, perm)
        return perm

    def dfs(depth):
        print len(depth)
        #print depth[len(depth)-1][0]
        start=6*(depth[len(depth)-1][0]/6+1)
        for x in range (start, start+12):
            #print x
            perm=cp(depth[len(depth)-1][1])
            move(x%18, perm)
            if cond(perm):
                depth.append([x%18, perm])
                return 0
            elif perm==mat:
                if x==start+11:
                    depth.pop()
                    return 1
                continue
            elif len(depth)==10:
                if x==start+11:
                    depth.pop()
                    return 1
                continue
            depth.append([x%18, perm])
            stat=dfs(depth)
            if stat==1 or stat==2:
                if x==start+11:
                    depth.pop()
                    return 1
                continue
            elif stat==0:
                return 0

    def calc_perm2index(perm):
        temp=cp(corn)
        index=0
        for i in range (0,7):
            cor=calc_col2code(perm[(i/4)][(i/2)%2][i%2])
            for j in range(i+1, 8):
                temp[j].remove(cor)
            index=index+(temp[i].index(cor)*fact(7-i))
        #print index
        return index

    def cond(perm):
        '''
        if not(perm[0][0][0][0]==perm[0][1][0][0] and \
               perm[0][1][0][0]==perm[1][0][0][0] and \
               perm[1][0][0][0]==perm[1][1][0][0]) :
            return False
        if not(perm[0][0][1][0]==perm[0][1][1][0] and \
               perm[0][1][1][0]==perm[1][0][1][0] and \
               perm[1][0][1][0]==perm[1][1][1][0]) :
            return False      
        if not(perm[0][0][0][1]==perm[0][0][1][1] and \
               perm[0][0][1][1]==perm[0][1][0][1] and \
               perm[0][1][0][1]==perm[0][1][1][1]) :
            return False
        if not(perm[1][0][0][1]==perm[1][0][1][1] and \
               perm[1][0][1][1]==perm[1][1][0][1] and \
               perm[1][1][0][1]==perm[1][1][1][1]) :
            return False
        if not(perm[0][0][0][2]==perm[1][0][0][2] and \
               perm[1][0][0][2]==perm[0][0][1][2] and \
               perm[0][0][1][2]==perm[1][0][1][2]) :
            return False
        if not(perm[0][1][0][2]==perm[1][1][0][2] and \
               perm[1][1][0][2]==perm[0][1][1][2] and \
               perm[0][1][1][2]==perm[1][1][1][2]) :
            return False
        return True        

        '''
        plane=0
        while plane<3 :
            x=0
            while x<2 :
                y=0
                while y<2 :
                    z=0
                    while z<2 :
                        if mat[x][y][z][plane] != mat[0][0][0][plane] and mat[x][y][z][plane] != opp[mat[0][0][0][plane]]:
                            break
                        z=z+1
                    if z<2 :
                        break
                    y=y+1
                if y<2 :
                    break
                x=x+1
            if x==2 :
                print True
                return True
            plane = plane +1
        #print False, len(perms)            
        return False
        
        '''
        if perm==[[[[0, 1, 2], [3, 2, 0]], [[5, 4, 3], [4, 2, 1]]], [[[3, 4, 2], [5, 4, 1]], [[3, 5, 0], [1, 5, 0]]]]:
            print "Yes"
            return True
        else:
            return False
        '''
    
    
    base=[]
    perms=[[]]
    if cond(mat):
        return inst
    
    for x in range (0,18):
        perm=cp(mat)
        base.append([x, move(x, perm)])
        perm=cp(base[x][1])
        if cond(perm) :
            return inst

    print base
        
    moves=["U", "U2", "U'", "D", "D2", "D'", "L", "L2", "L'", "R", "R2", "R'", "F", "F2", "F'", "B", "B2", "B'"]
    inst=[-1 for x in range (0,11)]

    for x in range (0,18) :
        print "-----", x, "-----"
        perms[0]=cp(base[x])
        if (dfs(perms)==0):
            print "Yes"
            break

    for x in perms:
        inst.append(x[0])

        
    return inst
