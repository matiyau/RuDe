def steps() :
    turns=["x", "x2", "x'", "y", "y2", "y'", "U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'", "RESET"]
    print "SETTING UP ..."
    import cubeCns
    import cubeSlv_GraphIDA as IDA    
    
    from time import sleep
    import serial    
    import pickle 
    
    #Arduino = serial.Serial("/dev/ttyUSB0", 115200)
    try:
        Arduino = serial.Serial("/dev/ttyACM0", 115200)
    except:
        try:
           Arduino = serial.Serial("/dev/ttyUSB0", 115200)
        except:
            try:
               Arduino = serial.Serial("/dev/ttyACM1", 115200)
            except:
                try:
                   Arduino = serial.Serial("/dev/ttyUSB1", 115200)
                except:
                    print "Error Connecting Arduino"
                    Arduino=7
                    #return 0
                
    sleep(4)

    print "\nRESETTING GRIPPERS."
    Arduino.write("*15#")
    
    
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
    
    solution="*"+"".join('<'+str(k) for k in Algo)+"#"
    print solution
    Arduino.write(solution)
    if Arduino.read(1)!='N':
        print "Cube not solved"
        return 0
    
    print '\n*** Cube Solved ***'

steps()
    
    
