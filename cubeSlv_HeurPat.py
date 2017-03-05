def steps () :
    from copy import deepcopy as cp
    from math import factorial as fact
    from threading import Thread
    import cubeSfy as cS
    import time
    
    #List of orientations of goal state
    goal=[[[[0,1,2],[5,1,2]],[[0,1,3],[5,1,3]]],[[[0,4,2],[5,4,2]],[[0,4,3],[5,4,3]]]]

    #List of corners available at each position
    corn=[i for i in range (0,7)]

    heur=[[[[[[[chr(11) for f in range (0,3)] for e in range (0,3)] for d in range (0,3)] for c in range (0,3)] for b in range (0,3)] for a in range (0,3)] for i in range (0,5040)]
    
    #List of moves
    moves=["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]

    #List of threads
    thr=[Thread for i in range (0,21)]

    #Function to interpret the data stored in the file
    def decode(k):
        for j in range (k*240, (k+1)*240):
            temp[j]=list(temp[j])
            #print len(temp[j])
            for a in range (0,3):
                for b in range (0,3):
                    for c in range (0,3):
                        for d in range (0,3):
                            for e in range (0,3):
                                for f in range (0,3):
                                    pos = 243*a + 81*b + 27*c + 9*d + 3*e + f
                                    if pos%2==0:
                                        heur[j][a][b][c][d][e][f]=chr((ord(temp[j][pos/2])-32)/16)
                                    else:
                                        heur[j][a][b][c][d][e][f]=chr((ord(temp[j][pos/2])-32)%16)

    #Function to write the data to a file
    def encode():
        with open('DBPat', 'wb') as pattern:
            for j in range(0,fact(7)):
                count=0
                for a in range (0,3):
                    for b in range (0,3):
                        for c in range (0,3):
                            for d in range (0,3):
                                for e in range (0,3):
                                    for f in range (0,3):
                                        if count%2==0:
                                            val_char=16*ord(heur[j][a][b][c][d][e][f])+32
                                        else:
                                            val_char=val_char+ord(heur[j][a][b][c][d][e][f])
                                            #print val_char
                                            pattern.write(chr(val_char))
                                        count=count+1                
                pattern.write(chr(val_char))
                pattern.write('\n')
            return

    
    #Function to perform a particular move on the cube
    def move(x, perm):
        if x/3==0 :
            cS.u(x%3+1, perm)
        elif x/3==1 :
            cS.r(x%3+1, perm)
        elif x/3==2 :
            cS.f(x%3+1, perm)
        return perm

    #Function to find index of 0 or 5 colour code in a corner
    def ind(cor):
        #print 'ind'
        if 0 in cor:
            #print '0'
            return cor.index(0)
        else:
            #print '5'
            return cor.index(5)
    
    #Calculate corner code from its colours
    def calc_col2code(cor):
        add = cor[0] + cor[1] + cor[2] - 3
        return (add/5)+(((add%5)**3 + 17*(add%5))/6 - (add%5)**2)-1

    #Return value of heuristic of a partcular permutation in the pattern list
    def hst_ret(perm):
        return ord(heur[calc_perm2index(perm)][ind(perm[0][0][1])][ind(perm[0][1][0])][ind(perm[0][1][1])][ind(perm[1][0][0])][ind(perm[1][0][1])][ind(perm[1][1][0])])
    
    #Assign heuristic value to a particular premutation heuristic in the pattern list
    def hst_asn(perm, val):
        #print val,
        #print calc_perm2index(perm), ind(perm[0][0][0]), ind(perm[0][0][1]), ind(perm[0][1][0]), ind(perm[0][1][1]), ind(perm[1][0][0]), ind(perm[1][0][1]), ind(perm[1][1][0])
        heur[calc_perm2index(perm)][ind(perm[0][0][1])][ind(perm[0][1][0])][ind(perm[0][1][1])][ind(perm[1][0][0])][ind(perm[1][0][1])][ind(perm[1][1][0])]=chr(val)
        
    #Initialize environment for DFS
    def init_dfs(y):
        print '-', y, '-'
        perms=[[]]
        perms[0]=cp(base[y])
        #print perms[0][1]
        hst_asn(perms[0][1], 1)
        dfs(perms, y)

    #Perform a depth-first algorithm on a list
    def dfs(depth, o):
        hst=len(depth)
        #print hst
        #print depth[len(depth)-1][0]
        start=3*(depth[hst-1][0]/3+1)
        for x in range (start, start+6):
            #print x
            perm=cp(depth[hst-1][1])
            move(x%9, perm)
            #print hst_ret(perm), hst
            if hst_ret(perm) > (hst+1):
                #print hst
                hst_asn(perm, hst+1)
                depth.append([x%9, cp(perm)])                            
                if hst==10:
                    depth.pop()
                else:
                    dfs(depth, o)
        if hst==2:
            print o
        depth.pop()
        return 2
    
    #Calculate the permutation from its index number
    def calc_perm2index(perm):
        temp=cp(corn)
        index=0
        for i in range (1,7):
            cor=calc_col2code(perm[(i/4)][(i/2)%2][i%2])
            index=index+(temp.index(cor)*fact(7-i))            
            temp.remove(cor)
        #print index
        return index

    print 'Start'
    print time.time()

    with open('PatternDB', 'rb') as pattern:
        temp=pattern.readlines()
        
    for i in range (0,21):
        try:
            thr[i]=Thread(target=decode, args=(i,))
            thr[i].start()
        except:
            print "Error", i

    for i in range (0,21):
        thr[i].join()

    print time.time()               

    print heur[786][2][0][1][2][2]
    
    hst_asn(goal, 0)
    base=[]
    for y in range (0,9):
        perm=cp(goal)
        base.append([y, cp(move(y, perm))])
        #print len(base)

    #time.sleep(3600)
    for y in range (0,9):           
        thr[y]=Thread(target=init_dfs, args=(y,))
        thr[y].start()

    for y in range (0,9):
        thr[y].join()

    '''with open('PatternDB', 'wb') as pattern:
        pickle.dump(heur, pattern)'''
    
    encode()
    
    
    for i in range (0,5040) :
        for a in range (0,3):
            for b in range (0,3):
                for c in range (0,3):
                    for d in range (0,3):
                        for e in range (0,3):
                            for f in range (0,3):
                                if heur[i][a][b][c][d][e][f]==12:
                                    print i,a,b,c,d,e,f
        
    print "Complete"

steps()
    
        
        
