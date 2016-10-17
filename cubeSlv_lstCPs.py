def steps(mat, inst) :
    import cubeSfy as cS
    import cubeRot as cR
    last_lay=[mat[0][1][0], mat[1][1][0], mat[1][1][1], mat[0][1][1]]
    '''
    last_lay1=[mat[0][0][0], mat[1][0][0], mat[1][0][1], mat[0][0][1]]
    for i in last_lay :
        print i
    print '\n'
    for i in last_lay1 :
        print i
    #'''
    def seq() :
        inst.append(cR.r(-1, mat))     # R
        inst.append(cR.u(1, mat))     # U'
        inst.append(cR.l(1, mat))     # L'
        inst.append(cR.u(-1, mat))     # U
        inst.append(cR.r(1, mat))     # R'
        inst.append(cR.u(1, mat))     # U'
        inst.append(cR.l(-1, mat))     # L
        
    for j in range(0,4) :
        if (mat[0][0][0][0] in last_lay[j]) and (mat[0][0][0][1] in last_lay[j]) :
            break
    for k in range(1,4) :
        if (mat[1][0][0][0] in last_lay[(j+k)%4]) and (mat[1][0][0][1] in last_lay[(j+k)%4]) :
            break
    for l in range(1,4) :
        if (mat[1][0][1][0] in last_lay[(j+l)%4]) and (mat[1][0][1][1] in last_lay[(j+l)%4]) :
            break
    #print j, k, l    
    if k==1 and l==2 :
        inst.extend(cS.u(-j, mat))
    elif k==2 and l==1 :
        inst.extend(cS.u(2-j, mat))
        seq()
    elif k==2 and l==3 :
        inst.extend(cS.u(-j-1, mat))
        seq()
        inst.extend(cS.u(2, mat))
    elif k==3 and l==2 :
        inst.extend(cS.u(-j-1, mat))
        seq()
        seq()
    elif k==1 and l==3 :
        inst.extend(cS.u(-j+1, mat))
        seq()
    elif k==3 and l==1 :
        inst.extend(cS.u(-j, mat))
        seq()
        inst.extend(cS.u(2, mat))



        

