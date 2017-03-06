def steps() :
    turns=["x", "x2", "x'", "y", "y2", "y'", "U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]
    print "SETTING UP ..."
    import cubeCns
    import cubeSlv_GraphIDA as IDA    
    
    from time import sleep
    import serial    
    import pickle 
    
    Arduino = serial.Serial("/dev/ttyACM0", 115200)
    sleep(1)
    
    print "\nCONSTRUCTING CUBE ...\nPlease Display The Mentioned Sides To The Camera."
    Cube = cubeCns.matrixForm(Arduino)
    with open('Matrix', 'rb') as comb:
        Cube=pickle.load(comb)

    print Cube
    
    print "\nCOMPUTING SOLUTION ..."
    DB=IDA.setup()
    Algo=IDA.main(Cube, DB)
    print "\nBEST SOLUTION :"
    print [turns[i] for i in Algo]
    
    print "\nSOLVING CUBE ..."
    Arduino.write("*"+"".join('<'+str(k) for k in Algo)+"#")
    if Arduino.read(1)!='N':
        print "Cube not solved"
        return 0
    
    print '\n*** Cube Solved ***'

steps()
    
    
