def percHardMallet(x,y,r=2,prop=7,c='black',**args):
    """symbol für harten schlägel
    x,y ist der mittelpunkt des kopfes
    r ist dessen radius
    prop ist die länge des stiels als verhältnis zu r"""
    d.append(dw.Circle(x,y,r,fill=c,**args))
    d.append(dw.Line(x,y,x,y+prop*r,stroke=c,stroke_width=r/5,**args))

def buerste(x=10,y=10,y_space=10,sw1fac=0.2,sw2fac=0.1,c='black',**args):
    """schlagzeugsymbol für bürste
    sw1fac ist für die waagerechte linie
    sw2fac ist für die haare / borsten
    beides sind relationen zum y_space
    x,y ist links oben"""
    sw1 = y_space*sw1fac
    sw2 = y_space*sw2fac
    l = y_space*2
    h = y_space*0.6
    d.append(dw.Line(x,y,x+l,y,stroke=c,stroke_width=sw1,**args))
    numborst = 9
    for i in range(numborst):
        xb = x+i*l/(numborst-1)
        d.append(dw.Line(xb,y,xb,y+h,stroke=c,stroke_width=sw2,**args))

def hand(x=20,y=20,siz=12,c='black',sw=0.75,**args):
    """hand als schlagzeugsymbol
    x,y ist in der mitte
    siz ist die gesamtgröße horizontal und vertikal"""
    p1 = x-siz/2,y
    p2 = x+siz*.1,y-siz*.5
    p3 = x+siz*.2,y-siz*.3
    p4 = x+siz*.3,y-siz*.1
    p5 = x-siz*.2,y+siz/2
    c1 = x,y-siz
    c2 = x+siz*.9,y-siz*1.3 #zeigefinger
    c3a = x+siz*.8,y-siz*1.3 #mittel
    c3b = x+siz*1,y-siz*1
    c4a = x+siz*.9,y-siz*1  #ring
    c4b = x+siz*1.2,y-siz*.9
    c5 = x+siz*1,y-siz*.7  #kleiner finger
    c6 = x+siz*.9,y-siz*.2
    p = dw.Path(fill='none',stroke=c,stroke_width=sw)
    p.M(*p1)
    p.C(*c1,*c2,*p2)
    p.C(*c3a,*c3b,*p3)
    p.C(*c4a,*c4b,*p4)
    p.C(*c5,*c6,*p5)
    d.append(p)

def kralle(x=20,y=20,siz=12,c='black',sw=0.75,sw2=1,**args):
    """hand mit kratzenden fingernägeln als schlagzeugsymbol
    x,y ist in der mitte
    siz ist die gesamtgröße horizontal und vertikal
    sw2 ist die dicke der nägel / krallen"""
    p1 = x-siz/2,y
    p2 = x+siz*.1,y-siz*.5
    p3 = x+siz*.2,y-siz*.3
    p4 = x+siz*.3,y-siz*.1
    p5 = x-siz*.2,y+siz/2
    c1 = x,y-siz
    c2 = x+siz*.9,y-siz*1.3 #zeigefinger
    c3a = x+siz*.8,y-siz*1.3 #mittel
    c3b = x+siz*1,y-siz*1
    c4a = x+siz*.9,y-siz*1  #ring
    c4b = x+siz*1.2,y-siz*.9
    c5 = x+siz*1,y-siz*.7  #kleiner finger
    c6 = x+siz*.9,y-siz*.2
    p = dw.Path(fill='none',stroke=c,stroke_width=sw)
    p.M(*p1)
    p.C(*c1,*c2,*p2)
    p.C(*c3a,*c3b,*p3)
    p.C(*c4a,*c4b,*p4)
    p.C(*c5,*c6,*p5)
    d.append(p)
    k1 = p2[0]+siz*.15,p2[1]-siz*.3
    k1a = k1[0]+siz*.3,k1[1]-siz*.3
    k2 = p3[0]+siz*.35,p3[1]-siz*.5
    k2a = k2[0]+siz*.32,k2[1]-siz*.3
    k3 = p4[0]+siz*.38,p4[1]-siz*.5
    k3a = k3[0]+siz*.35,k3[1]-siz*.3
    k4 = p4[0]+siz*.3,p4[1]-siz*.15
    k4a = k4[0]+siz*.3,k4[1]-siz*.25
    d.append(dw.Line(*k1,*k1a,stroke=c,stroke_width=sw2,stroke_linecap='round'))
    d.append(dw.Line(*k2,*k2a,stroke=c,stroke_width=sw2,stroke_linecap='round'))
    d.append(dw.Line(*k3,*k3a,stroke=c,stroke_width=sw2,stroke_linecap='round'))
    d.append(dw.Line(*k4,*k4a,stroke=c,stroke_width=sw2,stroke_linecap='round'))
