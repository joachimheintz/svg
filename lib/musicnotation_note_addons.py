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

def kratzgliss(x1=10,y1=10,x2=50,y2=10,h=4,swfac=1,prd=1,c='black',**args):
    """h ist die maximale höhe, p die periode
    ist im moment nur für waagerechte gliss; später nochmal die y-linie reinbringen
    h * swfac * 0.2 = stroke_width"""
    from random import uniform
    p = dw.Path(fill='none',stroke=c,stroke_width=h*swfac*.2,**args)
    p.M(x1,y1)
    x = x1
    while x <= x2:
        y = y1 + uniform(-h,h) #hier später y korrekt ermitteln
        x += prd
        p.L(x,y)
    d.append(p)
    
def krackelinie(x1=10,y1=10,x2=50,y2=10,hmin=3,hmax=4,prdmin=1.5,prdmax=3,swfac=1,c='black',**args):
    """eine krackel linie aus alternierenden oben-unten zacken.
    hmin und hmax ist die minimale und maximale höhe (auch nach unten)
    prdmin und prdmax ist die minimale und maximale periode
    ist im moment nur für waagerechte (y1=y2) definiert; später nochmal die y-linie reinbringen
    h * swfac * 0.2 = stroke_width"""
    from random import uniform
    p = dw.Path(fill='none',stroke=c,stroke_width=hmax*swfac*.2,**args)
    p.M(x1,y1)
    x = x1
    f = -1
    while x <= x2:
        h = uniform(hmin,hmax) * f
        y = y1 + h #hier später y korrekt ermitteln
        x += uniform(prdmin,prdmax)
        f *= -1
        p.L(x,y)
    d.append(p)

def varVibr(x1=10,y=30,x2=200,h=10,prd1=2,prdfac=2,c='black',**args):
    """macht ein vibrato mit variabler frequenz
    h ist die höhe des ausschlags
    prd1 ist die periodendauer am anfang
    prdfac ist der faktor für die veränderung der periodendauer"""
    p = dw.Path(fill='none',stroke=c,**args)
    p.M(x1,y)
    x = x1
    prd = prd1
    while x < x2:
        ptarget = x+prd,y
        c1 = x+prd/2,y-h
        c2 = x+prd/2,y+h
        p.C(*c1,*c2,*ptarget)
        x += prd
        prd *= prdfac
    d.append(p)

def triller(xstart=10,y=20,xend=100,siz=10,h=4,prd=2,swtr=.8,swline=.5,c='black',**args):
    """ein triller. siz ist die ungefähre höhe der schrift.
    h ist die amplitude des trillerzeichen, prd seine periode
    swtr, swline ist stroke width von der schrift und von der linie
    x,y ist links unten"""
    x = xstart
    xr = x+siz/3
    p1 = x,y-siz #t oben
    c1 = x-siz/8,y+siz/6
    c2 = x+siz/6,y
    p2 = x+siz/6,y-siz/8 #t unten
    p3 = x-siz/6,y-siz*.66 #schrägstrich vom t
    p4 = x+siz/6,y-siz*.66
    p5 = xr,y #r unten
    p6 = xr,y-siz*.55
    p7 = xr+siz/4,p6[1]
    c7 = xr+siz/8,p7[1]+siz/6
    p = dw.Path(fill='none',stroke=c,stroke_width=swtr,**args)
    p.M(*p1).C(*c1,*c2,*p2)
    p.M(*p3).L(*p4)
    p.M(*p5).L(*p6).Q(*c7,*p7)
    d.append(p)
    p = dw.Path(fill='none',stroke=c,stroke_width=swline,**args)
    p.M(*p7)
    x = p7[0]
    y = p7[1]
    while x <= xend-prd:
        x0 = x
        xc1 = x+prd
        xc2 = x+prd
        x += prd*2
        yc1 = p7[1]-h
        yc2 = p7[1]+h
        p.C(xc1,yc1,xc2,yc2,x,y)
    d.append(p)


