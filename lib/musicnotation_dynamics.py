def mezzo(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """musical notation for m=mezzo
    the height is 1/2 of siz
    x,y is bottom left
    swfac is relation to siz: sw = siz/12"""
    sw = siz/12
    h = siz*1/2
    xdif = h/2 
    p1 = x,y-h #anfang li ob
    p2 = x,y #li unt
    c3 = x, y-h
    p3 = x+xdif/2,y-h #halber weg oben
    c4 = x+xdif,y-h
    p4 = x+xdif,y #unt mitte
    c5 = x+xdif,y-h
    p5 = x+xdif*1.5,y-h
    c6 = x+xdif*2,y-h
    p6 = x+xdif*2,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.L(*p2)
    p.Q(*c3,*p3)
    p.Q(*c4,*p4)
    p.Q(*c5,*p5)
    p.Q(*c6,*p6)
    d.append(p)

def forte(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """musical notation for f=forte
    the height is siz but left goes below
    x,y is bottom left on the imagined line
    swfac is relation to siz: sw = siz/12"""
    sw = siz/12
    pfict = x,y #never used
    wdth = siz*.35
    x1 = x+wdth #rechts aussen
    y1 = y-siz*.9
    x2 = x+wdth*.7 #höchster punkt
    y2 = y-siz
    x3 = x+wdth*.1 #tiefster punkt
    y3 = y+siz*.25 
    x4 = x-wdth*.1
    y4 = y+siz*.15
    c2 = x1,y2
    c3a = x+wdth*.3,y-siz
    c3b = x+wdth*.2,y+siz*.2
    c4 = x4,y3
    ys = y-siz*1/2
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(x1,y1)
    p.Q(*c2,x2,y2)
    p.C(*c3a,*c3b,x3,y3)
    p.Q(*c4,x4,y4)
    p.M(x,ys)
    p.H(x+wdth*.8)
    d.append(p)

def piano(x=20,y=20,siz=12,c='black',swfac=1,**args):
    """musical notation for piano
    x,y is in left base line
    top and bottom is approx half of size
    swfac is relation to siz: sw = siz/12"""
    sw = siz/12
    h = siz/2 #nach oben
    p1 = x-h/8,y-h #kleiner schörkel links
    p2 = x, y-h*.9 #rechts daneben
    p3 = x-h/2, y+h*1.3 #ganz unten
    p4 = x,y-h/8 #beim schreiben zuletzt, auf der grundlinie
    c1 = x - h/8, y - h*1.15
    c2 = p4
    c3 = x+h, y-h*1.5
    c4 = x+h, y+h/4
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p3)
    p.M(*p2)
    p.C(*c3,*c4,*p4)
    d.append(p)

def mezzoforte(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """mezzo and forte"""
    xdist = siz*.66
    mezzo(x-xdist/2,y,siz,c,swfac,**args)
    forte(x+xdist/2,y,siz,c,swfac,**args)
    
def mezzopiano(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """mezzo and piano"""
    xdist = siz*.7
    mezzo(x-xdist/2,y,siz,c,swfac,**args)
    piano(x+xdist/2,y,siz,c,swfac,**args)

def fortissimo(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """musical dynamics"""
    xdist = siz*.33
    forte(x-xdist/2,y,siz,c,swfac,**args)
    forte(x+xdist/2,y,siz,c,swfac,**args)

def pianissimo(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """musical dynamics"""
    xdist = siz*.5
    piano(x-xdist/2,y,siz,c,swfac,**args)
    piano(x+xdist/2,y,siz,c,swfac,**args)

def piano3(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """pianissisimo (ppp)"""
    xdist = siz*.5
    piano(x-xdist/2,y,siz,c,swfac,**args)
    piano(x+xdist/2,y,siz,c,swfac,**args)
    piano(x+xdist*1.5,y,siz,c,swfac,**args)

def cresc(x=10,y=30,xend=30,yend=30,h=10,sw=0.4,c='black',hstart=0,**args):
    """crescendo
    x,y ist in der anfangspunkt
    xend,yend ist die mitte am ende
    h ist die gesamthöhe des cresc am ende
    hstart ist für den fall, dass das cresc nicht bei ganz geschlossener klammer beginnt
    """
    p = dw.Path(stroke=c,fill='none',stroke_width=sw)
    yendtop = yend-h/2
    yendbot = yend+h/2
    p.M(xend,yendtop)
    if hstart==0:p.L(x,y)
    else: p.L(x,y-hstart/2).M(x,y+hstart/2)
    p.L(xend,yendbot)
    d.append(p)
    
def dim(x=10,y=30,xend=30,yend=30,h=10,sw=0.4,c='black',**args):
    """diminuendo
    x,y ist in der mitte am anfang
    xend,yend ist der endpunkt
    h ist die gesamthöhe am anfang"""
    p = dw.Path(stroke=c,fill='none',stroke_width=sw)
    ystarttop = y-h/2
    ystartbot = y+h/2
    p.M(x,ystarttop)
    p.L(xend,yend)
    p.L(x,ystartbot)
    d.append(p)
    
