def steps() :
    print "SETTING UP ..."
    import cubeCns
    import cubeSlv_GraphIDA as IDA
    '''
    import cubeSlv_fst as F
    import cubeSlv_lstCPs as LC1
    import cubeSlv_lstCFx as LC2
    import cubeSlv_lstOrn as LF
    '''
    import pickle
    #import serial

    Algo = []
    Arduino = 3#serial.Serial("/dev/ttyACM0")
    #Arduino.baudrate = 38400
    
    print "\nCONSTRUCTING CUBE ...\nPlease Display The Mentioned Sides To The Camera."
    Cube = cubeCns.matrixForm(Arduino)
    with open('Matrix', 'rb') as comb:
        Cube=pickle.load(comb)
        

    print Cube
    IDA.steps(Cube, Algo)
    print "\nCOMPUTING SOLUTION ..."
    '''F.steps(Cube, Algo)
    LC1.steps(Cube, Algo)
    LC2.steps(Cube, Algo)
    LF.steps(Cube, Algo)

    print "\nSOLUTION :"
    ardAlgo = '*(1)(' + str(len(Algo)) + ')'
    for i in range(0,len(Algo)) :
        #print Algo[i], ", ",
        ardAlgo = ardAlgo + '(' + str(Move.index(Algo[i])) + ')'
    ardAlgo = ardAlgo + '#'
    #print '\n' + ardAlgo
    Arduino.write(ardAlgo)'''
    print Algo    
    print '\n*** Cube Solved ***'


steps()
    
    
