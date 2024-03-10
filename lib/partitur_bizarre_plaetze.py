# hier ein paar spezielle elemente der partitur von 'bizarre plaetze'

def jh(x=20,y=40,siz=12,c='black',swfac=1,**args):
    """dem herrn heintz sein logo
    x,y ist der links fuß vom h"""
    sw = siz*swfac/12
    p1 = x-siz*.2,y-siz*.4
    p2 = x-siz*.3,y+siz*.5
    p3 = x,y-siz
    p4 = x,y
    p5 = x+siz*.5,y+siz*.1
    c1 = x+siz*.5,y-siz*.6
    c2 = x+siz*.5,y+siz*.3
    c5 = x+siz*.5,y-siz*1
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(*p1).C(*c1,*c2,*p2)
    p.M(*p3).L(*p4).Q(*c5,*p5)
    d.append(p)

def jh2022(x=20,y=20,siz=12,c='black',swfac=1,rotate=20,**args):
    jh(x,y,siz,c,swfac,transform='rotate(%d %d %d)'%(rotate,x,y),**args)
    x1,y1 = x-siz,y+siz*1.1
    zwei(x1,y1,siz,c,swfac,transform='rotate(%d %d %d)'%(rotate,x,y),**args)
    x2,y2 = x1+10,y1
    null(x2,y2,siz,c,swfac,transform='rotate(%d %d %d)'%(rotate,x,y),**args)
    x3,y3 = x2+5,y1
    zwei(x3,y3,siz,c,swfac,transform='rotate(%d %d %d)'%(rotate,x,y),**args)
    x4,y4 = x3+6,y1
    zwei(x4,y4,siz,c,swfac,transform='rotate(%d %d %d)'%(rotate,x,y),**args)
    
def bp_A(x=20,y=20,wd=27,ht=23,**args):
    """element A von bizarre plaetze, für analytische partitur
    glissando von unten nach oben
    xy ist oben links"""
    sw_innen = wd/10
    sw_rahmen = wd/20
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.85
    p2 = x+wd*.9,y+ht*.15
    glisscurve(*p1,*p2,sw=sw_innen,**args)

def bp_B(x=20,y=20,wd=27,ht=23,**args):
    """element B von bizarre plaetze, für analytische partitur
    hohes grisseln
    xy ist oben links"""
    sw_rahmen = wd/20
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.2
    p2 = x+wd*.9,y+ht*.2
    from random import seed
    seed(7)
    kratzgliss(*p1,*p2,h=2,prd=.4,**args)

def bp_C(x=20,y=20,wd=27,ht=23,**args):
    """element C von bizarre plaetze, für analytische partitur
    zwei töne fallend in mittellage
    xy ist oben links"""
    sw_rahmen = wd/20
    r = wd/15
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.3,y+ht*.35
    p2 = x+wd*.7,y+ht*.65
    dot(*p1,r,**args)
    dot(*p2,r,**args)
    
def bp_D(x=20,y=20,wd=27,ht=23,**args):
    """element D von bizarre plaetze, für analytische partitur
    zackenlinie
    xy ist oben links"""
    sw_rahmen = wd/20
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.5
    p2 = x+wd*.9,y+ht*.5
    from random import seed
    seed(7)
    krackelinie(*p1,*p2,h=2,hmin=2,hmax=3,prdmin=1,prdmax=1,swfac=1.2,**args)

def bp_E(x=20,y=20,wd=27,ht=23,**args):
    """element E von bizarre plaetze, für analytische partitur
    zwei töne steigend von mittel nach hoch
    xy ist oben links"""
    sw_rahmen = wd/20
    r = wd/15
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.3,y+ht*.45
    p2 = x+wd*.7,y+ht*.3
    dot(*p1,r,**args)
    dot(*p2,r,**args)
    
def bp_F(x=20,y=20,wd=27,ht=23,**args):
    """element F von bizarre plaetze, für analytische partitur
    glissando von mitte nach unten
    xy ist oben links"""
    sw_innen = wd/10
    sw_rahmen = wd/20
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.4
    p2 = x+wd*.9,y+ht*.85
    glisscurve(*p1,*p2,sw=sw_innen,**args)

def bp_G(x=20,y=20,wd=27,ht=23,**args):
    """element G von bizarre plaetze, für analytische partitur
    tiefe linie
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/10
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.8
    p2 = x+wd*.9,y+ht*.8
    line(*p1,*p2,stroke_width=sw_linie,**args)

def bp_H(x=20,y=20,wd=27,ht=23,**args):
    """element G von bizarre plaetze, für analytische partitur
    hohe linie
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/10
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.2
    p2 = x+wd*.9,y+ht*.2
    line(*p1,*p2,stroke_width=sw_linie,**args)

def bp_I(x=20,y=20,wd=27,ht=23,**args):
    """element I von bizarre plaetze, für analytische partitur
    in der mitte kleiner werdene linien
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/30
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.5
    linlen = ht*.5
    offset = wd/7
    for i in range(10):
        vline(p1[0]+offset*i,p1[1]-linlen/2,linlen,sw=sw_linie,**args)
        linlen *= .83
        offset *= .95

def bp_K(x=20,y=20,wd=27,ht=23,**args):
    """element G von bizarre plaetze, für analytische partitur
    mittlere linie
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/10
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.5
    p2 = x+wd*.9,y+ht*.5
    line(*p1,*p2,stroke_width=sw_linie,**args)

def bp_L(x=20,y=20,wd=27,ht=23,**args):
    """element L von bizarre plaetze, für analytische partitur
    quasi kantilene
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/30
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.1,y+ht*.9
    p2 = x+wd*.3,y+ht*.3
    p3 = x+wd*.5,y+ht*.6
    p4 = x+wd*.7,y+ht*.2
    p5 = x+wd*.9,y+ht*.8
    smooth_curve([*p1,*p2,*p3,*p4,*p5],sw=sw_linie,**args)

def bp_M(x=20,y=20,wd=27,ht=23,**args):
    """element M von bizarre plaetze, für analytische partitur
    drei mittlere linien
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_linie = wd/12
    kasten(x,y,wd,ht,sw=sw_rahmen)
    linlen = wd*.2
    offset = wd*.3
    ylin = y+ht*.5
    for i in range(3):
        hline(x+wd*.1+offset*i,ylin,linlen,sw=sw_linie,**args)

def bp_N(x=20,y=20,wd=27,ht=23,**args):
    """element N von bizarre plaetze, für analytische partitur
    drei mal
    xy ist oben links"""
    sw_rahmen = wd/20
    sw_schrift = wd/20
    h_schrift = 12
    kasten(x,y,wd,ht,sw=sw_rahmen)
    p1 = x+wd*.2,y+ht*.8
    p2 = x+wd*.55,y+ht*.82
    p3 = x+wd*.75,y+ht*.5
    fac = (h_schrift / 12) * sw_schrift
    drei(*p1,swfac=fac)
    line(*p2,*p3,stroke_width=sw_schrift)
    line(p2[0],p3[1],p3[0],p2[1],stroke_width=sw_schrift)

