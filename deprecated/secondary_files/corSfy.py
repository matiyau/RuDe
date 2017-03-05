def l(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.l(-1, corn))
    else :
        inst_prt.append(corRot.l(1, corn))
    return  inst_prt

def r(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.r(-1, corn))
    else :
        inst_prt.append(corRot.r(1, corn))
    return  inst_prt

def u(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.u(-1, corn))
    else :
        inst_prt.append(corRot.u(1, corn))
    return  inst_prt

def d(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.d(-1, corn))
    else :
        inst_prt.append(corRot.d(1, corn))
    return  inst_prt

def f(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.f(-1, corn))
    else :
        inst_prt.append(corRot.f(1, corn))
    return  inst_prt

def b(vec, corn) :
    inst_prt=[]
    import corRot
    vec = (vec)%4
    if vec < 3 :
        for i in range(0,vec) :
            inst_prt.append(corRot.b(-1, corn))
    else :
        inst_prt.append(corRot.b(1, corn))
    return  inst_prt
