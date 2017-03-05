def steps(mat, inst) :
    import cubeSfy as cS
    import cubeRot as cR
    def seq(dirn):
        inst.extend(cR.u(1, mat))      # U'
        inst.extend(cR.l(dirn, mat))   # dirn=1 : L' ; dirn=-1 : L
        inst.extend(cR.u(-1, mat))     # U
        inst.extend(cR.l(-dirn, mat))  # dirn=-1 : L ; dirn=1 : L'
    def corFix(conds) :
        while not(set(conds) < set(mat[0][1][1])) and mat[0][1][1][2]!=5 :
            if set(conds) < set(mat[0][1][1]) :
                inst.extend(cR.r(1, mat))
                #if mat[0][1][1][2]==5 :
                    #break
                inst.extend(cR.u(1, mat))
            elif set(conds) < set(mat[0][1][0]) :
                if mat[0][1][0][0]==5 :
                    inst.extend(cR.r(-1, mat))
                else :
                    inst.extend(cR.u(1, mat))
            elif set(conds) < set(mat[1][1][0]) :
                inst.extend(cR.u(1, mat))
            elif set(conds) < set(mat[1][1][1]) :
                inst.extend(cR.u(-1, mat))
            elif set(conds) < set(mat[0][0][0]) :
                inst.extend(cR.l(-1, mat))
            elif set(conds) < set(mat[0][0][1]) :
                inst.extend(cR.l(1, mat))
            elif set(conds) < set(mat[1][0][0]) :
                inst.extend(cR.r(1, mat))
                inst.extend(cR.u(1, mat))
            elif set(conds) < set(mat[1][0][1]) :
                inst.extend(cR.r(-1, mat))
                inst.extend(cR.u(-1, mat))
    corFix([5])
    if 5 in mat[1][0][1] and mat[0][1][1][1] in mat[1][0][1] :
        inst.extend(cS.r(2, mat))
    inst.extend(cR.u(1, mat))
    inst.extend(cR.r(1, mat))
    corFix([5, mat[1][0][1][2]])
    inst.extend(cR.r(-1, mat))
    inst.extend(cR.u(1, mat))
    inst.extend(cS.r(2, mat))
    corFix([5, mat[1][0][0][1]])
    inst.extend(cR.u(1, mat))
    if 5 in mat[1][1][0] :
        inst.extend(cR.u(1, mat))
        inst.extend(cR.l(-1, mat))
        inst.extend(cR.u(-1, mat))
    if 5 in [mat[0][0][0][1], mat[0][1][0][1], mat[0][1][1][1], mat[0][0][1][1]] :
        k=0
        while mat[0][0][1][1] != 5 :
            cS.l(1, mat)
            k=k+1
        cS.l(-k, mat)
        inst.extend(cS.l(k, mat))
        seq(1)
    elif 5 in [mat[0][0][0][0][0], mat[0][1][0][2], mat[0][1][1][0], mat[0][0][1][2]] :
        k=0
        while mat[0][1][0][2] != 5 :
            cS.l(1, mat)
            k=k+1
        cS.l(-k, mat)
        inst.extend(cS.l(k, mat))
        seq(-1)
    else :
        k=0
        while mat[0][1][1][2] != 5 :
            cS.l(1, mat)
            k=k+1
        cS.l(-k, mat)
        inst.extend(cS.l(k, mat))
    inst.extend(cR.u(-1, mat))
    inst.extend(cS.l(2, mat))    
