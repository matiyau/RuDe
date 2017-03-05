from math import factorial as fact
#from threading import Thread
#import pickle
#import time


#th=[Thread for i in range (0,56)]

def steps():
    #List of heuristic functions for each and every cube orientation and permutation
    with open('PatternDB', 'wb') as pattern:
        for c in range(0,fact(7)):
            for b in range (0,(3**6)/2):
                pattern.write(chr(236))
            pattern.write(chr(224))
            pattern.write('\n')
        #print ' Done', i

print 'Start'
'''
heur=[[[[[[[[chr(11) for g in range (0, 3)] for f in range (0,3)] for e in range (0,3)] for d in range (0,3)] for c in range (0,3)] for b in range (0,3)] for a in range (0,3)] for i in range (0,40320)]

print time.time()

with open ('DBPat', 'wb') as pattern:
    pickle.dump(heur, pattern)


for a in range(0,56):
    try:
        th[i]=Thread(target=steps, args=(a,))
        th[i].start()
    except:
        print "Error in", j

for a in range(0,56):
    th[i].join()

'''

steps()
#print time.time()
print 'End'
