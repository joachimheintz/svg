def note(x=10,y=10,y_space=10,**args):
    """note with xy as center
    for color: fill='gray' or fill='#444'"""
    r = y_space/2
    p = dw.Path(**args)
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)

def not2tel(x=20,y=30,dirlen=1,y_space=10,swfac=1,swfac_head=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    """half note with xy as center
    dirlen=1 means in normal length (y_space*2.4) upwards
    dirlen=-1.1 means in length 2.64*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swfac_head is stroke width of the head line, as relation to the line * 1.5
    **args go to the head
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)
    returns the x,y of end of the line to use in 8th notes etc"""
    sw = y_space * swfac * 0.1 
    swhead = sw*swfac_head*1.5
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(stroke=c,fill='none',stroke_width=swhead,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: 
        endxy = p2[0],p2[1]-dirlen*y_space*2.4
        d.append(dw.Line(*p2,*endxy,stroke=c,stroke_width=sw))
    else: 
        endxy = p1[0],p1[1]-dirlen*y_space*2.4
        d.append(dw.Line(*p1,*endxy,stroke=c,stroke_width=sw))
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += y_space/2
    return endxy

def not4tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """4ter note with xy as center
    dirlen=1 means in normal length (y_space*2.5) upwards
    dirlen=-1.1 means in length 2.75*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    **args go to the head
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)
    returns the x,y of end of the line to use in 8th notes etc"""
    sw = y_space * swfac * 0.1
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: 
        endxy = p2[0],p2[1]-dirlen*y_space*2.5
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*endxy,stroke=c,stroke_width=sw))
    else: 
        endxy = p1[0],p1[1]-dirlen*y_space*2.5
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*endxy,stroke=c,stroke_width=sw))
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += y_space/2
    return endxy

def not8tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """8th note with xy as center
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*2.75,
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*2.75
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        return pbottom

def not16tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,swflagfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """16th note with xy as center
    dirlen=1 means in normal length (y_space*3) upwards
    dirlen=-1.1 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space*0.2
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac * 0.2
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*3
        ptop2 = p2[0],ptop[1]+swflag*3
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*3
        pbottom2 = p1[0],pbottom[1]-swflag*3
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        return pbottom

def not32tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,swflagfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """32th note with xy as center
    dirlen=1 means in normal length (y_space*3.25) upwards
    dirlen=-1.2 means in length 3.9*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space*0.2
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac * 0.2
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*3.25
        ptop2 = p2[0],ptop[1]+swflag*3
        ptop3 = p2[0],ptop2[1]+swflag*3
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop3,ptop3[0]+dxflag,ptop3[1]+dyflag,stroke=c,stroke_width=swflag))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*3.25
        pbottom2 = p1[0],pbottom[1]-swflag*3
        pbottom3 = p1[0],pbottom2[1]-swflag*3
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom3,pbottom3[0]+dxflag,pbottom3[1]-dyflag,stroke=c,stroke_width=swflag))
        return pbottom

def gruppe(notlist=[10,50,40,50,60,50],balken=[1,-2,1],dotlist=[],balkdick=1,balkspace=1,balklen=1,
           dirlen=1.5,y_space=10,swfac=1,c='#444',dotspace=1,dotsiz=1,**args):
    """eine gruppe von noten die unter einem balken steht
    notlist: sind die x,y werte
    balken: gibt an wie viele balken bei jeder note. negativ = nach links
    dotlist: entweder leer oder zahlen für punktierung (0=keine) 
    balkdick: dicke der balken als relation zum y_space
    balkspace: abstand zwischen zwei balken als relation zur dicke
    balklen: länge eines einzelbalkens als relation zu y_space
    die übrigen parameter sind wie bei not4tel"""
    endpoints = []
    dick = balkdick * y_space/3
    bspace = dick * balkspace * 2
    blen = y_space * 0.5 * balklen
    # zuerst die noten als viertel malen
    for i in range(len(balken)):
        x,y = notlist[i*2], notlist[i*2+1]
        if dotlist: dt = dotlist[i]
        else: dt = 0
        ex,ey = not4tel(x,y,dirlen,y_space,swfac,dt,c,**args)
        endpoints.extend((ex,ey))
    # balken hinzufügen für alle ausser die letzte note
    for i in range(len(balken)-1):
        balk = balken[i]
        nextbalk = abs(balken[i+1])
        val = 1
        while val <= abs(balk):
            # anfangspunkt
            x1,y1 = endpoints[i*2],endpoints[i*2+1]+bspace*(val-1)
            # entweder durchziehen bis zur nächsten note
            if nextbalk >= val: x2,y2 = endpoints[(i+1)*2],endpoints[(i+1)*2+1]+bspace*(val-1)
            # oder nur einen teilstrich
            else: x2,y2 = x1+bspace*balk/abs(balk),y1
            d.append(dw.Line(x1,y1,x2,y2,stroke=c,stroke_width=dick))
            val += 1
    # letzte note
    i = len(balken)-1
    balk = balken[i]
    prevbalk = abs(balken[i-1])
    val = 1
    while val <= abs(balk):
        # wo sind wir
        x1,y1 = endpoints[i*2],endpoints[i*2+1]+bspace*(val-1)
        # nur etwas nach links ziehen wenn mehr balken als note links
        if val > prevbalk:
            x2,y2 = x1-bspace,y1
            d.append(dw.Line(x1,y1,x2,y2,stroke=c,stroke_width=dick))
        val += 1

def hals4tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,dotted=0,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    r = y_space/2
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*2.5,
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += y_space/2
    return rpoint

def hals8tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += y_space/2
    return rpoint

def hals16tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*3
        ptop2 = x,ptop[1]+swflag*3
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*3
        pbottom2 = x,pbottom[1]-swflag*3
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += y_space/2
    return rpoint

def hals32tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*3.25
        ptop2 = x,ptop[1]+swflag*3
        ptop3 = x,ptop2[1]+swflag*3
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop3,ptop3[0]+dxflag,ptop3[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*3.25
        pbottom2 = x,pbottom[1]-swflag*3
        pbottom3 = x,pbottom2[1]-swflag*3
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom3,pbottom3[0]+dxflag,pbottom3[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += y_space/2
    return rpoint


#old definition of quarter note --- keep for compatibility
def viertel(x=10,y=10,dirlen=1,y_space=10,c='#444',sw=1,**args):
    """4ter note with xy as center
    dirlen=1 means in normal length (y_space*2.5) upwards
    dirlen=-1.1 means in length 2.75*yspace downwards
    sw is stroke width of the line
    **args go to the head"""
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: d.append(dw.Line(p2[0],p2[1]+y_space/5,p2[0],p2[1]-dirlen*y_space*2.5,stroke=c,stroke_width=sw))
    else: d.append(dw.Line(p1[0],p1[1]-y_space/5,p1[0],p1[1]-dirlen*y_space*2.5,stroke=c,stroke_width=sw))

def paus4tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """viertel pause (ha!)
    x,y ist in der mitte der glyphe
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= 1.3 # skalierung zur anpassung an die anderen pausen
    p1 = x+y_space*.1,y+y_space*1.2
    p2 = x+y_space/4,y+y_space*.45
    p3 = x-y_space*.1,y-y_space*.15
    p4 = x+y_space/5,y-y_space*.5
    p5 = x-y_space*.0,y-y_space*.9
    c2 = x-y_space/2,y+y_space/4
    c5 = x-y_space*.0,y-y_space*.7
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c2,*p2)
    p.L(*p3).L(*p4)
    p.Q(*c5,*p5)
    d.append(p)
    if dotted > 0:
        x = x+dotspace*y_space*0.66
        y = y
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/8,fill=c))
            x += dotspace*y_space/2

def paus8tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """achtel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*0.8,y-y_space*1.2
    p2 = x+y_space,y-y_space
    p3 = x,y+y_space*1.5
    c1 = x,y-y_space/4
    c2 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p3)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2
    
def paus16tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """sechzehntel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*0.8,y-y_space*1.4 #oben links
    p2 = x+y_space,y-y_space*1.2 #oben rechts
    p3 = x+y_space*.5,y-y_space*.6 #zweites faehnchen rechts
    p4 = x-y_space*.9,y-y_space*.8 #zweites faehnchen links
    p5 = x,y+y_space*1.5 #unten
    c1 = x,y-y_space*.5
    c2 = x,y-y_space*.1
    c3 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.L(*p3)
    p.Q(*c2,*p4)
    p.M(*p3)
    p.Q(*c3,*p5)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2

def paus32tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """32igstel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*.7,y-y_space*1.6 #erstes faehnchen links
    p2 = x+y_space,y-y_space*1.4 #erstes rechts
    p3 = x-y_space*.9,y-y_space*1 #zweites faehnchen links
    p4 = x+y_space*.5,y-y_space*.8 #zweites rechts
    p5 = x-y_space*.9,y-y_space*.4 #drittes faehnchen links
    p6 = x+y_space*.3,y-y_space*.3 #drittes rechts
    p7 = x,y+y_space*1.5 #unten
    c1 = x,y-y_space*.9
    c2 = x,y-y_space*.5
    c3 = x,y-y_space*.1
    c4 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1).Q(*c1,*p2)
    p.M(*p3).Q(*c2,*p4)
    p.M(*p5).Q(*c3,*p6)
    p.M(*p2).L(*p4).L(*p6)
    p.Q(*c4,*p7)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2
