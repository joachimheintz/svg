def tie(x=10,y=90,xend=100,yend=10,dir=1,sw=1,c='black',**args):
    """tie (haltebogen) between two notes
    dir=1 means bowing downwards, dir=1 upwards
    larger number means more bowing
    thick results in the thickness"""
    p = dw.Path(fill=c,stroke=c,stroke_width=sw,**args)
    xdiff = xend-x
    ydiff = xdiff*.2*dir
    p1 = x,y
    p2 = xend,yend
    pbow = x+xdiff/2,y+ydiff
    c1 = pbow
    c2 = pbow[0],pbow[1]+ydiff/5
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p1)
    d.append(p)

def accent(x=10,y=10,y_space=10,sw=1,c='black',**args):
    """a normal accnt sign, like >
    x,y is in the middle of the sign"""
    w = y_space*0.8
    p1 = x-w*0.4,y-y_space/4
    p2 = x+w*0.6,y
    p3 = x-w*0.4,y+y_space/4
    d.append(dw.Lines(*p1,*p2,*p3,stroke=c,stroke_width=sw,fill='none',**args))

def nlet(x1=10,y1=10,x2=30,y2=10,sw=0.3,h=4,textspace=7,margin=1,
         text='3',fontsiz=7,fontfam='Cantarell',**args):
    """triplet or any other number
    sw = strokewidth, h = height (positive=downwards)
    textspace is in the middle, margin to each side"""
    textpos = x1 + (x2-x1) / 2, y1 + (y2-y1) / 2
    d.append(dw.Text(text,fontsiz,*textpos,text_anchor='middle',
                     font_family=fontfam,font_style='italic',dominant_baseline='middle'))
    xstart = x1 + margin
    xmidl = textpos[0] - textspace/2
    xmidr = textpos[0] + textspace/2
    xend = x2 - margin
    ymid = textpos[1]
    p = dw.Path(stroke='black',stroke_width=sw,fill='none')
    p.M(xstart,y1+h).L(xstart,y1).L(xmidl,ymid)
    p.M(xmidr,ymid).L(xend,y2).L(xend,y2+h)
    d.append(p)

def nlets(x1=10,y1=10,x2=30,y2=10,num=1,sw=0.3,h=4,textspace=7,margin=1,
         text='3',fontsiz=7,fontfam='Cantarell',**args):
    """adds num nlets to each other"""
    xdist = x2-x1
    ydist = y2-y1
    for i in range(num):
        nlet(x1,y1,x2,y2,sw,h,textspace,margin,
         text,fontsiz,fontfam,**args)
        x1 += xdist
        x2 += xdist
        y1 += ydist
        y2 += ydist

def glisscurve(x=10,y=90,xend=100,yend=10,c='black',sw=1,sdiff=1,**args):
    """sw = stroke-width
    sdiff ist effektiv die dicke der linie in der mitte"""
    sadd = sdiff/50
    p = dw.Path(fill=c,stroke=c,stroke_width=sw)
    xdiff = xend-x
    ydiff = yend-y
    p1 = x,y
    p2 = xend,yend
    c1 = x+xdiff*.6,y+ydiff*.2
    c2 = x+xdiff*(.6-sadd),y+ydiff*(.2+sadd)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p1)
    d.append(p)

def kratzgliss(x1=10,y1=10,x2=50,y2=10,h=4,swfac=0.2,prd=1,c='black',**args):
    """h ist die maximale höhe, p die periode
    ist im moment nur für waagerechte gliss; später nochmal die y-linie reinbringen
    h * swfac = stroke_width"""
    from random import uniform
    p = dw.Path(fill='none',stroke=c,stroke_width=h*swfac,**args)
    p.M(x1,y1)
    x = x1
    while x <= x2:
        y = y1 + uniform(-h,h) #hier später y korrekt ermitteln
        x += prd
        p.L(x,y)
    d.append(p)
    

