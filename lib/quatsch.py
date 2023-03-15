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

def zwei(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """die zahl zwei
    x,y ist links unten"""
    sw = siz * swfac / 12 
    p1 = x-siz*.1,y-siz*.7
    p2 = x-siz*.1,y-siz*.1
    p3 = x+siz*.6,y-siz*.1
    c1 = x+siz*1,y-siz*1
    c2 = x+siz*.2,y+siz*.2
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(*p1).Q(*c1,*p2).Q(*c2,*p3)
    d.append(p)

def null(x=20,y=20,siz=12,c='black',swfac=1,**args):
    """die zahl null
    x,y ist unten"""
    sw = siz * swfac / 12 
    p1 = x,y-siz*.8
    p2 = x,y+siz*.05
    c1a = x-siz*.4,y-siz*.75
    c1b = x-siz*.4,y
    c2a = x+siz*.4,y
    c2b = x+siz*.4,y-siz*.75
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(*p1).C(*c1a,*c1b,*p2).C(*c2a,*c2b,*p1)
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
    
