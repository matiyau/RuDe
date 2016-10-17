def steps (mat, inst) :
    import cubeSfy as cS
    import cubeRot as cR
    for k in range(0, 4) :
        if mat[0][0][0][0]==mat[0][1][0][0] :
            break
        cR.u(1, mat)
    cS.u(k, mat)
    inst.extend(cS.u(-k, mat))
    
        
            

                
        
        
