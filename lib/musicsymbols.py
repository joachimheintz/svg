def percHardMallet(x,y,r=2,prop=7,c='black',**args):
    """symbol für harten schlägel
    x,y ist der mittelpunkt des kopfes
    r ist dessen radius
    prop ist die länge des stiels als verhältnis zu r"""
    d.append(dw.Circle(x,y,r,fill=c,**args))
    d.append(dw.Line(x,y,x,y+prop*r,stroke=c,stroke_width=r/5,**args))

def percSoftMallet(x=20,y=50,r=2,prop=7,swfac=1,c='black',**args):
    """symbol für weichen schlägel
    x,y ist der mittelpunkt des kopfes
    r ist dessen radius
    prop ist die länge des stiels als verhältnis zu r
    sw = swfac * r / 4"""
    sw = swfac * r / 4
    d.append(dw.Circle(x,y,r,stroke=c,fill='none',stroke_width=sw,**args))
    d.append(dw.Line(x,y+r,x,y+prop*r,stroke=c,stroke_width=sw,**args))

def perc2SoftMallets(x=20,y=50,r=2,prop=6,swfac=1,c='black',rotate=25,**args):
    """zwei soft mallets als zeichen dass sie in einer hand gehalten werden
    symbol für weichen schlägel
    x,y ist der mittelpunkt des kopfes
    r ist dessen radius
    prop ist die länge des stiels als verhältnis zu r
    sw = swfac * r / 4"""
    yrot = y+(prop*r)*.66
    percSoftMallet(x,y,r,prop,swfac,c,transform='rotate(%d %d %d)'%(rotate,x,yrot))
    percSoftMallet(x,y,r,prop,swfac,c,transform='rotate(%d %d %d)'%(-rotate,x,yrot))

def percDrumstick(x=10,y=10,l=20,lfac=0.25,swfac=1,sw2fac=2,c='black',**args):
    """symbol for drum sticks
    x,y ist oben
    swfac ist das verhältnis von sw (stroke width) zu l:
      sw = swfac * l / 20
    lfac ist der dicke anteil unten
    sw2fac ist der faktor um den der untere teil dicker ist als sw"""
    sw = swfac * l / 20
    d.append(dw.Line(x,y,x,y+l,stroke=c,stroke_width=sw,**args))
    d.append(dw.Line(x,y+l-l*lfac,x,y+l,stroke=c,stroke_width=sw*sw2fac,**args))
    
def percSuperball(x=20,y=50,r=2,dotfac=0.5,prop=7,swfac=1,c='black',**args):
    """symbol für superball
    x,y ist der mittelpunkt des kopfes
    r ist dessen radius
    dotfac ist das verhältnis des radius vom punkt in der mitte zum radius des kopfes
    prop ist die länge des stiels als verhältnis zu r
    sw = swfac * r / 4"""
    sw = swfac * r / 4
    rdot = r*dotfac
    d.append(dw.Circle(x,y,r,stroke=c,fill='none',stroke_width=sw,**args))
    d.append(dw.Line(x,y+r,x,y+prop*r,stroke=c,stroke_width=sw,**args))
    d.append(dw.Circle(x,y,rdot,fill=c,**args))

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

def kreisLinks(x=20,y=20,r=7,swfac=1,c='black',**args):
    """ein kreis mit pfeil nach links
    sw = swfac * r / 10
    x,y ist mitte des kreises"""
    sw = swfac * r / 10
    alen = r*.8
    d.append(dw.Circle(x,y,r,fill='none',stroke=c,stroke_width=sw,**args))
    d.append(dw.Lines(x+r-alen/2,y+alen/2, x+r,y ,x+r+alen/2,y+alen/2,fill='none',stroke=c,stroke_width=sw,**args))

def kreisRechts(x=20,y=20,r=7,swfac=1,c='black',**args):
    """ein kreis mit pfeil nach rechts
    sw = swfac * r / 10
    x,y ist mitte des kreises"""
    sw = swfac * r / 10
    alen = r*.8
    d.append(dw.Circle(x,y,r,fill='none',stroke=c,stroke_width=sw,**args))
    d.append(dw.Lines(x-r-alen/2,y+alen/2, x-r,y ,x-r+alen/2,y+alen/2,fill='none',stroke=c,stroke_width=sw,**args))

def kreisStartEnd(x=20,y=20,r=7,start=45,end=-225,swfac=1,c='black',**args):
    """ein kreis mit einem definierten anfang und ende, und einem pfeil in dieser richtung
    winkel: 0=oben, positiv=clockwise, negativ=linksrum
    wenn end>start: rechtsrum, und umgekehrt
    sw = swfac * r / 10
    x,y ist mitte des kreises"""
    sw = swfac * r / 10
    alen = r*.8
    linelen = r*.66 #länge der linien anfang bzw ende
    # anfangs und endpunkt berechnen
    from math import sin,cos,radians
    alpha,beta = radians(-start+90),radians(-end+90) #winkel bezogen auf x achse
    x_start,y_start = x+cos(alpha)*r, y-sin(alpha)*r
    x_end,y_end = x+cos(beta)*r, y-sin(beta)*r
    # die beiden linien ziehen
    x_startline_1,y_startline_1 = x_start+cos(alpha)*linelen/2, y_start-sin(alpha)*linelen/2
    x_startline_2,y_startline_2 = x_start-cos(alpha)*linelen/2, y_start+sin(alpha)*linelen/2
    x_endline_1,y_endline_1 = x_end+cos(beta)*linelen/2, y_end-sin(beta)*linelen/2
    x_endline_2,y_endline_2 = x_end-cos(beta)*linelen/2, y_end+sin(beta)*linelen/2
    d.append(dw.Line(x_startline_1,y_startline_1,x_startline_2,y_startline_2,stroke=c,stroke_width=sw))
    d.append(dw.Line(x_endline_1,y_endline_1,x_endline_2,y_endline_2,stroke=c,stroke_width=sw))
    # draw the circle line
    if abs(start-end) > 180: large_arc=1
    else: large_arc=0
    if end > start: 
        sweep=1
        startarrow = end-30 #winkel wo der pfeil anfängt
    else: 
        sweep=0
        startarrow = end+30
    p = dw.Path(stroke=c,stroke_width=sw,fill='none',**args)
    p.M(x_start,y_start)
    p.A(r,r,0,large_arc,sweep,x_end,y_end)
    d.append(p)
    # arrow
    gamma = radians(-startarrow+90)
    x_startarrow,y_startarrow = x+cos(gamma)*r, y-sin(gamma)*r
    x_startarrow_1,y_startarrow_1 = x_startarrow+cos(gamma)*linelen/3, y_startarrow-sin(gamma)*linelen/3
    x_startarrow_2,y_startarrow_2 = x_startarrow-cos(gamma)*linelen/3, y_startarrow+sin(gamma)*linelen/3
    d.append(dw.Lines(x_startarrow_1, y_startarrow_1,x_end,y_end,x_startarrow_2,y_startarrow_2,fill=c,**args))

