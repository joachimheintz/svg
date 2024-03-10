def ledger(x=10,y=10,num=1,y_space=10,leng=20,sw=1,color='black'):
    """draws num ledgers
    x,y is the center of the first one, the others are below"""
    for i in range(num):
        d.append(dw.Line(x-leng/2,y,x+leng/2,y,stroke=color,stroke_width=sw))
        y += y_space
    
def stave(x=10,y=10,len=200,y_space=10,color='black',sw=1,numlines=5):
    """draws a stave.  x,y are top left"""
    for i in range(numlines):
        d.append(dw.Line(x,y+i*y_space,x+len,y+i*y_space,stroke=color,stroke_width=sw))

def violinClef(x=10,y=10,linspace=10,color='black',sw=2,ottava=0,swottfac=1,**args):
    """draws a violin clef.  x,y are top left of the stave
    ottava=1 ist 8 oben, ottava=-1 ist 8 unten
    swottfac ist stroke width vom okavzeichen als verhältnis zum anderen (default=1)"""
    p1 = x+linspace/2,y+linspace*3.5
    c1a = x+linspace*4,y+linspace
    c1b = x+linspace/3, y+linspace*6
    p2 = x+linspace/10,y+linspace*3
    c2a = x,y+linspace*2
    c2b = x+linspace*2,y-linspace
    p3 = x+linspace,y-linspace/2 #höchster punkt
    c3a = x,y-linspace/2
    c3b = x+linspace*2, y+linspace*4
    p4 = x+linspace/2,y+linspace*5
    c4a = x, y+linspace*5
    c4b = x+linspace/2, y+linspace*4.5
    p5 = x+linspace/2,y+linspace*4.5 #tiefster punkt
    p = dw.Path(stroke=color,stroke_width=sw,fill='none',**args)
    p.M(*p1)
    p.C(*c1a, *c1b, *p2)
    p.C(*c2a, *c2b, *p3)
    p.C(*c3a, *c3b, *p4)
    p.C(*c4a, *c4b, *p5)
    if ottava==1: acht(p3[0],p3[1]-sw,linspace*.75,color,linspace*1.25*0.12*sw*swottfac)
    if ottava==-1: acht(p5[0],p5[1]+sw+linspace+sw,linspace*.75,color,linspace*1.25*0.12*sw*swottfac)
    d.append(p)

def bassClef(x=10,y=10,linspace=10,color='black',sw=2,r=1):
    """draws a bass clef.  x,y are top left of the stave
    sw = stroke width, r = radius for two points"""
    p1 = x+linspace*.7,y+linspace*.8
    c1a = x+linspace*.9,y+linspace*1.1
    c1b = x+linspace*.5, y+linspace*1.3
    p2 = x+linspace*.4,y+linspace
    c2a = x+linspace*.2,y+linspace/2
    c2b = x+linspace*.6,y
    p3 = x+linspace*1,y+linspace/7
    c3a = x+linspace*2,y+linspace/2
    c3b = x+linspace, y+linspace*2
    p4 = x+linspace/5,y+linspace*3-linspace/7
    p = dw.Path(stroke=color,stroke_width=sw,fill='none')
    p.M(*p1)
    p.C(*c1a, *c1b, *p2)
    p.C(*c2a, *c2b, *p3)
    p.C(*c3a, *c3b, *p4)
    d.append(p)
    d.append(dw.Circle(x+linspace*1.7,y+linspace-r*3,r,stroke=color))
    d.append(dw.Circle(x+linspace*1.7,y+linspace+r*3,r,stroke=color))

