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
    
    
    perms=[[-1, mat]]
    if cond(perms[0][1]):
        return inst
    
    for x in range (0,18):
        perm=cp(perms[0][1])
        perms.append([x, move(x, perm)])
        perm=cp(perms[x+1][1])
        if cond(perm) :
            return inst
        
    moves=["U", "U2", "U'", "D", "D2", "D'", "L", "L2", "L'", "R", "R2", "R'", "F", "F2", "F'", "B", "B2", "B'"]
    while True:
        prev=(len(perms)-7)/12
        start=6*((perms[prev][0]/6)+1)
        for x in range (start, start+12):
            perm=cp(perms[prev][1])
            tag=x%18 
            perms.append([tag, move(tag, perm)])
            print len(perms)
            if cond(perm):
                prev=-1
                break
        if prev==-1:
            break

    prev=len(perms)-1
    while prev!=0:
        inst.append(moves[perms[prev][0]])
        prev=(prev-7)/12
        perms=perms[:prev+1]

    for x in range (0,len(inst)/2):
        temp=inst[x]
        inst[x]=inst[len(inst)-x-1]
        inst[len(inst)-x-1]=temp
    
    return inst
