def l(vec, mat) :
    inst_prt=[]
    import cubeRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(cubeRot.l(-1, mat))
    else :
        inst_prt.append(cubeRot.l(1, mat))
    return  inst_prt

def r(vec, mat) :
    inst_prt=[]
    import cubeRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(cubeRot.r(-1, mat))
    else :
        inst_prt.append(cubeRot.r(1, mat))
    return  inst_prt

def u(vec, mat) :
    inst_prt=[]
    import cubeRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(cubeRot.u(-1, mat))
    else :
        inst_prt.append(cubeRot.u(1, mat))
    return  inst_prt

def d(vec, mat) :
    inst_prt=[]
    import cubeRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(cubeRot.d(-1, mat))
    else :
        inst_prt.append(cubeRot.d(1, mat))
    return  inst_prt

