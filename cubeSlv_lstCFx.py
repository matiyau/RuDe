def steps (mat, inst) :
    import cubeSfy as cS
    import cubeRot as cR
    last_lay=[mat[0][1][0], mat[1][1][0], mat[1][1][1], mat[0][1][1]]    
    '''    
    for i in last_lay :
        print i
    #'''
    def seq_nor() :
        inst.append(cR.r(1, mat))     # R'
        inst.append(cR.u(1, mat))     # U'
        inst.append(cR.r(-1, mat))     # R
        inst.append(cR.u(1, mat))     # U'
        inst.append(cR.r(1, mat))     # R'
        inst.extend(cS.u(2, mat))     # U2
        inst.append(cR.r(-1, mat))     # R
    def seq_inv() :
        inst.append(cR.r(1, mat))     # R'
        inst.extend(cS.u(2, mat))     # U2
        inst.append(cR.r(-1, mat))     # R
        inst.append(cR.u(-1, mat))     # U
        inst.append(cR.r(1, mat))     # R'
        inst.append(cR.u(-1, mat))     # U
        inst.append(cR.r(-1, mat))     # R
    def seq_main() :
        for k in range(0, 4) :
            if mat[0][1][0][2]==0 :
                break
            cR.u(1, mat)
        if mat[1][1][0][0]==0 :
            cS.u(k, mat)
            inst.extend(cS.u(-k, mat))
            seq_nor()
        elif mat[1][1][0][1]==0 :
            cS.u(k, mat)
            inst.extend(cS.u(-k+2, mat))
            seq_inv()
            
    pos=[]
    for j in range(0, 4) :
        if last_lay[j][2]==0 :      #red
            pos.append(j)
    if len(pos)==1 :
        #print pos[0]
        seq_main()
    elif len(pos)==4 :
        pass
    elif len(pos)==2 :
        #print pos[0], pos[1]
        cS.u(3-pos[1], mat)
        if mat[1][1][0][2]==0 :
            if mat[1][1][1][1]==0 :
                cS.u(pos[1]-3, mat)
                inst.extend(cS.u(3-pos[1], mat))
                seq_nor()
            else :
                cS.u(pos[1]-3, mat)
                inst.extend(cS.u(5-pos[1], mat))
                seq_inv()
        else :
            if mat[1][1][0][0]==0 :
                cS.u(pos[1]-3, mat)
                inst.extend(cS.u(3-pos[1], mat))
                seq_nor()
                
            else :
                cS.u(pos[1]-3, mat)
                inst.extend(cS.u(5-pos[1], mat))
                seq_inv()
        seq_main()
    elif len(pos)==0 :
        if mat[1][1][0][0]==0 and mat[0][1][1][0]==0 :
            inst.extend(cS.u(2, mat))
            seq_inv()
        elif mat[1][1][0][0]!=0 and mat[0][1][1][0]!=0 :
            seq_nor()
        else:
            if mat[1][1][1][0]==0 :
                seq_nor()
            else :
                inst.extend(cS.u(2, mat))
                seq_inv()
        seq_main()
        
            

                
        
        
