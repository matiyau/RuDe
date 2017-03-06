from threading import Thread
import cubeSfy as cS
from math import factorial as fact
from copy import deepcopy as cp

def setup():
    heur=[[[[[[[chr(11) for f in range (0,3)] for e in range (0,3)] for d in range (0,3)] for c in range (0,3)] for b in range (0,3)] for a in range (0,3)] for i in range (0,5040)]

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
      

    with open('DBPat', 'rb') as pattern:
            temp=pattern.readlines()
            
    for i in range (0,21):
        try:
            thr[i]=Thread(target=decode, args=(i,))
            thr[i].start()
        except:
            print "Error", i

    for i in range (0,21):
        thr[i].join()

    return heur

def main (scramble, heur) :
    #List of corners
    corn=[i for i in range (0,7)]

    #List of moves
    moves=["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]

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
        #print perm
        return ord(heur[calc_perm2index(perm)][ind(perm[0][0][1])][ind(perm[0][1][0])][ind(perm[0][1][1])][ind(perm[1][0][0])][ind(perm[1][0][1])][ind(perm[1][1][0])])
    
    #Initialize environment for DFS
    def init_ida(y):
        #print '-', y, '-'
        perms=[[]]
        perms[0]=cp(base[y])
        #print perms[0][1]
        size=hst_ret(perms[0][1])
        print size
        if ida(perms, size)==0:
            #print "Solved"
            for i in range (0, len(perms)):
                soln[y].append(perms[i][0]+6)
        

    #Perform a depth-first algorithm on a list
    def ida(depth, rots):
        hst=len(depth)
        start=3*(depth[hst-1][0]/3+1)
        for x in range (start, start+6):
            #print x
            perm=cp(depth[hst-1][1])
            move(x%9, perm)
            #print hst_ret(perm), hst
            db_rots=hst_ret(perm)
            #print hst, db_rots, rots
            if db_rots > (rots-1):
                continue
            depth.append([x%9, cp(perm)])
            if db_rots==0:
                return 0
            if ida(depth, db_rots)==0:
                return 0
        depth.pop()
        return 2
    
    #Calculate the permutation from its index number
    def calc_perm2index(perm):
        temp=cp(corn)
        index=0
        for i in range (1,7):
            #print perm
            cor=calc_col2code(perm[(i/4)][(i/2)%2][i%2])
            index=index+(temp.index(cor)*fact(7-i))            
            temp.remove(cor)
        #print index
        return index

    base=[]
    for y in range (0,9):
        perm=cp(scramble)
        move(y, perm)
        if hst_ret(perm)<=(hst_ret(scramble)-1):
            base.append([y, cp(perm)])

    soln=[[] for i in range (0, len(base))]
    for y in range (0,len(base)):           
        #thr[y]=Thread(target=init_ida, args=(y,))
        #thr[y].start()
        init_ida(y)

    #for y in range (0,len(base)):
        #thr[y].join()

    pos=0
    for y in range (0,len(base)):
        if len(soln[y])<len(soln[pos]):
            pos=y
        elif len(soln[y])==len(soln[pos]):
            f_count=0
            for i in  soln[y]:
                if (i%3==4):
                    f_count=f_count+1
            for i in soln[pos]:
                if (i%3==4):
                    f_count=f_count-1
            if f_count<=0:
                pos=y
        
    return soln[pos]
#steps()
