def l(sgn, corn):
    x=0
    y=1
    z=1
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = x
        y_prev = int(0.5 + sgn*(0.5-z))
        z_prev = int(0.5 + sgn*(y-0.5))
        corn[x][y][z] = corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp
    

def r(sgn, corn):
    x=1
    y=1
    z=1
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = x
        y_prev = int(0.5 + sgn*(z-0.5))
        z_prev = int(0.5 + sgn*(0.5-y))
        corn[x][y][z]=corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp

def u(sgn, corn):
    x=1
    y=1
    z=1
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(0.5-z))
        y_prev = y
        z_prev = int(0.5 + sgn*(x-0.5))
        corn[x][y][z]=corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp

def d(sgn, corn):
    x=1
    y=0
    z=1
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(z-0.5))
        y_prev = y
        z_prev = int(0.5 + sgn*(0.5-x))
        corn[x][y][z]=corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp

def f(sgn, corn):
    x=1
    y=1
    z=1
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(y-0.5))
        y_prev = int(0.5 + sgn*(0.5-x))
        z_prev = z
        corn[x][y][z]=corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp

def b(sgn, corn):
    x=1
    y=1
    z=0
    temp=corn[x][y][z]
    for count in range(0,3) :
        x_prev = int(0.5 + sgn*(0.5-y))
        y_prev = int(0.5 + sgn*(x-0.5))
        z_prev = z
        corn[x][y][z]=corn[x_prev][y_prev][z_prev]
        x = x_prev
        y = y_prev
        z = z_prev
    corn[x][y][z]=temp

def full(face, sgn, corn) :
    inst_prt=[]
    if face=='up' :
        u(sgn, corn)
        d(sgn*(-1), corn)
    elif face=='down' :
        u(sgn*(-1), corn)
        d(sgn, corn)
    elif face=='left' :
        l(sgn, corn)
        r(sgn*(-1), corn)
    elif face=='right' :
        l(sgn*(-1), corn)
        r(sgn, corn)
    elif face=='front' :
        b(sgn*(-1), corn)
        f(sgn, corn)
    elif face=='back' :
        f(sgn*(-1), corn)
        b(sgn, corn)
    return inst_prt
        
