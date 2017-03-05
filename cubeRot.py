def l(sgn, mat):
    x=0
    y=1
    z=1
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = x
        y_prev = int(0.5 + sgn*(0.5-z))
        z_prev = int(0.5 + sgn*(y-0.5))
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][0]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][2]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[1]
    mat[x][y][z][0]=temp[2]
    mat[x][y][z][2]=temp[0]
    if sgn>0 :
        return "l'"
    else :
        return "l"
    

def r(sgn, mat):
    x=1
    y=1
    z=1
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = x
        y_prev = int(0.5 + sgn*(z-0.5))
        z_prev = int(0.5 + sgn*(0.5-y))
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][0]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][2]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[1]
    mat[x][y][z][0]=temp[2]
    mat[x][y][z][2]=temp[0]
    if sgn>0 :
        return "r'"
    else :
        return "r"

def u(sgn, mat):
    x=1
    y=1
    z=1
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(0.5-z))
        y_prev = y
        z_prev = int(0.5 + sgn*(x-0.5))
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][0]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][2]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[0]
    mat[x][y][z][0]=temp[1]
    mat[x][y][z][2]=temp[2]
    if sgn>0 :
        return "u'"
    else :
        return "u"

def d(sgn, mat):
    x=1
    y=0
    z=1
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(z-0.5))
        y_prev = y
        z_prev = int(0.5 + sgn*(0.5-x))
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][0]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][2]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[0]
    mat[x][y][z][0]=temp[1]
    mat[x][y][z][2]=temp[2]
    if sgn>0 :
        return "d'"
    else :
        return "d"

def f(sgn, mat):
    x=1
    y=1
    z=1
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(y-0.5))
        y_prev = int(0.5 + sgn*(0.5-x))
        z_prev = z
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][2]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][0]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[2]
    mat[x][y][z][0]=temp[0]
    mat[x][y][z][2]=temp[1]
    if sgn>0 :
        return "f'"
    else :
        return "f"

def b(sgn, mat):
    x=1
    y=1
    z=0
    temp=[mat[x][y][z][0], mat[x][y][z][1], mat[x][y][z][2]]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(0.5-y))
        y_prev = int(0.5 + sgn*(x-0.5))
        z_prev = z
        mat[x][y][z][1]=mat[x_prev][y_prev][z_prev][2]
        mat[x][y][z][2]=mat[x_prev][y_prev][z_prev][1]
        mat[x][y][z][0]=mat[x_prev][y_prev][z_prev][0]
        x = x_prev
        y = y_prev
        z = z_prev
    mat[x][y][z][1]=temp[2]
    mat[x][y][z][0]=temp[0]
    mat[x][y][z][2]=temp[1]
    if sgn>0 :
        return "b'"
    else :
        return "b"

def full(face, sgn, mat) :
    inst_prt=[]
    if face=='up' :
        inst_prt.append(u(sgn, mat))
        inst_prt.append(d(sgn*(-1), mat))
    elif face=='down' :
        inst_prt.append(u(sgn*(-1), mat))
        inst_prt.append(d(sgn, mat))
    elif face=='left' :
        inst_prt.append(l(sgn, mat))
        inst_prt.append(r(sgn*(-1), mat))
    elif face=='right' :
        inst_prt.append(l(sgn*(-1), mat))
        inst_prt.append(r(sgn, mat))
    elif face=='front' :
        inst_prt.append(f(sgn, mat))
        inst_prt.append(b(sgn*(-1), mat))
    elif face=='back' :
        inst_prt.append(f(sgn*(-1), mat))
        inst_prt.append(b(sgn, mat))
    return inst_prt  
