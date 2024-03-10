
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

def drei(x=10,y=20,siz=12,c='black',swfac=1,**args):
    """die zahl drei
    x,y ist links unten"""
    sw = siz * swfac / 12 
    p1 = x,y-siz*.95
    p2 = x+siz/10,y-siz*.6
    p3 = x,y-siz*.05
    c1a = x+siz*.55,y-siz*1.2
    c1b = x+siz*.55,y-siz*.55
    c2a = x+siz*.6,y-siz*.6
    c2b = x+siz*.6,y+siz*.2
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(*p1).C(*c1a,*c1b,*p2).C(*c2a,*c2b,*p3)
    d.append(p)

def acht(x=20,y=20,siz=12,c='black',swfac=1,**args):
    """die zahl acht
    x,y ist unten"""
    sw = siz * swfac / 12 
    p1 = x,y-siz #oben
    p2 = x,y #unten
    p3 = x,y-siz*.55 #mitte
    xd1 = .25
    xd2 = .33
    x1,x2,x3,x4 = x-siz*xd1,x+siz*xd2,x-siz*xd2,x+siz*xd1
    y1,y2,y3,y4 = y-siz*.99,y-siz*.63,y-siz*.47,y-siz*.01
    c1a = x1,y1
    c1b = x1,y2
    c2a = x2,y3
    c2b = x2,y4
    c3a = x3,y4
    c3b = x3,y3
    c4a = x4,y2
    c4b = x4,y1
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(*p1).C(*c1a,*c1b,*p3).C(*c2a,*c2b,*p2).C(*c3a,*c3b,*p3).C(*c4a,*c4b,*p1)
    d.append(p)

