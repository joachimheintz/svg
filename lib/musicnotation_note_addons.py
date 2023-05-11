def tie(x=10,y=10,xend=100,yend=10,dir=1,sw=1,c='black',thick=1,cp=0.5,**args):
    """tie (haltebogen) between two notes
    dir=1 means bowing downwards, dir=1 upwards
    larger number means more bowing
    thick results in the thickness
    cp: x value of control point (0-1), default 0.5"""
    p = dw.Path(fill=c,stroke=c,stroke_width=sw,**args)
    xdiff = xend-x
    ydiff = xdiff*.2*dir
    p1 = x,y
    p2 = xend,yend
    pbow = x+xdiff*cp,y+ydiff
    c1 = pbow
    c2 = pbow[0],pbow[1]+thick*ydiff/5
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p1)
    d.append(p)

def tie2(x=10,y=10,xend=100,yend=10,dir=1,sw=1,c='black',thick=1,c1=0,c2=1,**args):
    """haltebogen mit zwei kontrollpunkten c1 und c2 (0-1)
    dir=1 means bowing downwards, dir=1 upwards
    larger number means more bowing
    thick results in the thickness"""
    xdiff = xend-x
    cp1_x = x + xdiff*c1
    cp2_x = x + xdiff*c2
    p = dw.Path(fill=c,stroke=c,stroke_width=sw,**args)
    ydiff = xdiff*.2*dir
    p1 = x,y
    p2 = xend,yend
    pbow = x+xdiff/2,y+ydiff
    cp1 = cp1_x,y+ydiff
    cp2 = cp2_x,y+ydiff
    cp1a = cp1_x,cp1[1]+thick*ydiff/5
    cp2a = cp2_x,cp2[1]+thick*ydiff/5
    p.M(*p1)
    p.C(*cp1,*cp2,*p2)
    p.C(*cp2a,*cp1a,*p1)
    d.append(p)

def tie3(x=10,y=10,xend=100,yend=10,cpx=40,cpy=40,sw=1,c='black',thick=1,**args):
    """tie (haltebogen) mit kontrollpunkt als koordinaten
    dadurch können bögen leicht manuell festgelegt werden
    dir=1 means bowing downwards, dir=1 upwards
    larger number means more bowing
    thick results in the thickness"""
    p = dw.Path(fill=c,stroke=c,stroke_width=sw,**args)
    p1 = x,y
    p2 = xend,yend
    pbow = cpx,cpy
    c1 = pbow
    c2 = pbow[0]+thick*sw,pbow[1]+thick*sw
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

def tenuto(x=10,y=10,y_space=10,distfac=1,swfac=1,c='black',**args):
    """ein tenuto strich
    x,y ist die position der note
    y_space>0: oben, y_space<0: unten
    swfac ist das verhältnis zum y_space:
        stroke_width = abs(y_space) * 0.1 * swfac
    distfac modifiziert den abstand zur note"""
    yy = y - y_space  * distfac
    x1 = x - y_space * .6
    x2 = x + y_space * .7
    sw = abs(y_space) * 0.2 * swfac
    d.append(dw.Line(x1,yy,x2,yy,stroke=c,stroke_width=sw,**args))

def fermate(x=10,y=20,y_space=10,dir=1,swfac=1,c='black',thick=1,dotfac=1,**args):
    """eine fermate
    x,y ist da wo der punkt ist
    dir=-1 bedeutet von unten"""
    dotsiz = y_space * .2 * dotfac
    sw = y_space * .1 * swfac
    if dir==-1: rot=180
    else: rot=0
    d.append(dw.Circle(x,y,dotsiz,fill=c))
    p = dw.Path(fill=c,stroke=c,stroke_width=sw,
                transform='rotate(%f,%f,%f)'%(rot,x,y),**args)
    x1 = x-y_space
    x2 = x+y_space
    r = y_space
    r2 = r-y_space*.1*thick
    yy = y+y_space/5
    p1 = x1,yy
    p2 = x2,yy
    p.M(*p1)
    p.A(r,r,0,1,1,*p2)
    p.A(r,r2,0,1,0,*p1)
    q = p
    d.append(p)


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
    h * swfac * 0.2 = stroke_width"""
    from random import uniform
    m = (y2-y1) / (x2-x1)
    p = dw.Path(fill='none',stroke=c,stroke_width=h*swfac*.2,**args)
    p.M(x1,y1)
    x = x1
    while x <= x2:
        y = (x-x1)*m + y1 + uniform(-h,h)
        x += prd
        p.L(x,y)
    d.append(p)

def kratzgliss_q(xstart=10,ystart=10,xend=100,yend=50,xcp=50,ycp=10,h=4,swfac=1,prd=1,c='black',**args):
    """kratzgliss als quadratische bezier kurve mit dem kontrollpunkt xcp,ycp
    h ist die maximale höhe, p die periode
    h * swfac * 0.2 = stroke_width"""
    from random import uniform
    p = dw.Path(fill='none',stroke=c,stroke_width=h*swfac*.2,**args)
    p.M(xstart,ystart)
    x = xstart
    while x <= xend:
        y = getqbezier(x,xstart,ystart,xcp,ycp,xend,yend) + uniform(-h,h)
        x += prd
        p.L(x,y)
    d.append(p)

def kratzgliss_seg(xyseg=[10,20,50,20,100,30,150,10],hseg=[3,1,8,1],pseg=[1,2,3,2],sw=1,c='black',**args):
    """kratzglissando mit segmenten zwischen denen interpoliert wird
    xyseg: mindestens zwei segmente aus xy paaren
    hseg: genauso viele segmente für die höhe, oder konstanter wert
    pseg: genauso viele segmente für die periode, oder konstanter wert
    sw: ein wert für strke width, oder liste mit werten für die segmente"""
    from random import uniform
    # alle input parameter in listen umformen
    numseg = len(xyseg) // 2
    if not isinstance(hseg,list): hseg = [hseg]*numseg
    if not isinstance(pseg,list): pseg = [pseg]*numseg
    if not isinstance(sw,list): sw = [sw]*numseg
    # die x und y werte in eigene listen schreiben
    xseg = [xyseg[i*2] for i in range(numseg)]
    yseg = [xyseg[i*2+1] for i in range(numseg)]
    # anfangswerte setzen
    x,y,h,p,s = xseg[0],yseg[0],hseg[0],pseg[0],sw[0]
    indx = 1
    while x < xseg[-1]:
        # abstand zum nächsten x
        xnext = x+p
        # werte für y,h,p,sw dort
        ynext = yfrompoints(xnext,xseg[indx-1],yseg[indx-1],xseg[indx],yseg[indx])
        hnext = yfrompoints(xnext,xseg[indx-1],hseg[indx-1],xseg[indx],hseg[indx])
        pnext = yfrompoints(xnext,xseg[indx-1],pseg[indx-1],xseg[indx],pseg[indx])
        snext = yfrompoints(xnext,xseg[indx-1],sw[indx-1],xseg[indx],sw[indx])
        ynext += uniform(-h,h)
        # linie ziehen
        d.append(dw.Line(x,y,xnext,ynext,stroke=c,stroke_width=s,**args))
        # werte aktualisieren
        x,y,h,p,s = xnext,ynext,hnext,pnext,snext
        # ggf index raufsetzen aber niemals über die grenzen
        if x > xseg[indx]: indx += 1
        if indx >= len(xseg): indx = len(xseg)-1

def krackelinie(x1=10,y1=10,x2=50,y2=10,hmin=3,hmax=4,prdmin=1.5,prdmax=3,swfac=1,c='black',**args):
    """eine krackel linie aus alternierenden oben-unten zacken.
    hmin und hmax ist die minimale und maximale höhe (auch nach unten)
    prdmin und prdmax ist die minimale und maximale periode
    h * swfac * 0.2 = stroke_width"""
    from random import uniform
    m = (y2-y1) / (x2-x1)
    p = dw.Path(fill='none',stroke=c,stroke_width=hmax*swfac*.2,**args)
    p.M(x1,y1)
    x = x1
    f = -1
    while x <= x2:
        h = uniform(hmin,hmax) * f
        y = (x-x1)*m + y1 + h
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

def varVibr2(x1=10,y=30,x2=200,hmin=5,hmax=10,prdmin=3,prdmax=9,c='black',sw=1,**args):
    """macht ein vibrato mit variabler frequenz in brownscher bewegung
    hmin und hmax geben die höhe des ausschlags
    prdmin und prdmax geben die periodendauer"""
    from random import uniform
    hmaxdiff = hmax-hmin #maximale veränderung zwischen zwei perioden
    prdmaxdiff = prdmax-prdmin #dito
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(x1,y)
    x = x1
    h = (hmin+hmax) / 2 #mit den mittleren werten beginnen
    prd = (prdmin+prdmax) / 2
    while x < x2:
        # diese periode ausführen
        prd = brownian1(prd,prdmin,prdmax,prdmaxdiff)
        h = brownian1(h,hmin,hmax,hmaxdiff)
        ptarget = x+prd,y
        c1 = x+prd/2,y-h
        c2 = x+prd/2,y+h
        p.C(*c1,*c2,*ptarget)
        x += prd
    d.append(p)

def varVibr2_l(xstart=10,ystart=10,xend=100,yend=50,
               hmin=5,hmax=10,prdmin=3,prdmax=9,
               hmaxdiffac=1,prdmaxdiffac=1,mdiffac=2,c='black',sw=1,returnonly=0,**args):
    """wie varVibr2 aber als linie zwischen xystart und xyend
    mit hmaxdiffac und prdmaxdiffac lässt sich die maximale abweichung von einem
    zum nächsten schritt steuern
    mdiffac=2 bedeutet dass die steigung in einer periode zwischen m/2 und m*2 liegt
    gibt den pfad zurück
    wenn returnonly=1 wird NUR der pfad zurückgegeben"""
    from random import uniform
    hmaxdiff = (hmax-hmin) * hmaxdiffac #maximale veränderung zwischen zwei perioden
    prdmaxdiff = (prdmax-prdmin) * prdmaxdiffac #dito
    m = (yend-ystart) / (xend-xstart)
    m_maxdiff = ((m*mdiffac)-(m/mdiffac)) / 2
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(xstart,ystart)
    x,y = xstart,ystart
    h = (hmin+hmax) / 2 #mit den mittleren werten beginnen
    prd = (prdmin+prdmax) / 2 #damit es sich möglichst schnell bewegt
    mhier = m
    while x < xend:
        mhier = brownian1(mhier,m/mdiffac,m*mdiffac,m_maxdiff)
        xtarget = x+prd
        h = brownian1(h,hmin,hmax,hmaxdiff)
        ytarget = y+(xtarget-x)*mhier
        c1 = x+prd/2,ytarget-h
        c2 = x+prd/2,ytarget+h
        p.C(*c1,*c2,xtarget,ytarget)
        x = xtarget
        y = ytarget
        prd = brownian1(prd,prdmin,prdmax,prdmaxdiff)
    if returnonly==0: d.append(p)
    return p

def varVibr2_lseg(xyseg=[10,10,50,100,150,50],hmin=5,hmax=10,prdmin=3,prdmax=9,
               hmaxdiffac=1,prdmaxdiffac=1,mdiffac=2,c='black',sw=1,returnonly=0,**args):
    """wie varVibr2_l aber als xy segmente in xylis
    mit hmaxdiffac und prdmaxdiffac lässt sich die maximale abweichung von einem
    zum nächsten schritt steuern
    mdiffac=2 bedeutet dass die steigung in einer periode zwischen m/2 und m*2 liegt
    gibt den pfad zurück
    wenn returnonly=1 wird NUR der pfad zurückgegeben"""
    from random import uniform
    hmaxdiff = (hmax-hmin) * hmaxdiffac #maximale veränderung zwischen zwei perioden
    prdmaxdiff = (prdmax-prdmin) * prdmaxdiffac #dito
    numseg = len(xyseg) // 2
    # die x und y werte in eigene listen schreiben
    xseg = [xyseg[i*2] for i in range(numseg)]
    yseg = [xyseg[i*2+1] for i in range(numseg)]
    # anfangswerte setzen
    m = (yseg[1]-yseg[0]) / (xseg[1]-xseg[0])
    m_maxdiff = ((m*mdiffac)-(m/mdiffac)) / 2
    x,y = xseg[0],yseg[0]
    h = (hmin+hmax) / 2 
    prd = (prdmin+prdmax) / 2 
    mhier = m
    indx = 0
    # der pfad
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(x,y)
    # iterieren
    while x < xseg[-1]:
        mhier = brownian1(mhier,m/mdiffac,m*mdiffac,m_maxdiff)
        xtarget = x+prd
        h = brownian1(h,hmin,hmax,hmaxdiff)
        ytarget = y+(xtarget-x)*mhier
        c1 = x+prd/2,ytarget-h
        c2 = x+prd/2,ytarget+h
        p.C(*c1,*c2,xtarget,ytarget)
        x = xtarget
        y = ytarget
        prd = brownian1(prd,prdmin,prdmax,prdmaxdiff)
        # ggf index raufsetzen und steigung aktualisieren 
        if x > xseg[indx+1] and indx < len(xseg)-2:
            indx += 1
            m = (yseg[indx+1]-yseg[indx]) / (xseg[indx+1]-xseg[indx])
            m_maxdiff = ((m*mdiffac)-(m/mdiffac)) / 2
            mhier = m
    if returnonly==0: d.append(p)
    return p

def varVibr2_q(xstart=10,ystart=10,xend=100,yend=50,xcp=50,ycp=10,
               hmin=5,hmax=10,prdmin=3,prdmax=9,c='black',sw=1,**args):
    """wie varVibr2 aber als quadratische bezierkurve für das ganze"""
    from random import uniform
    hmaxdiff = hmax-hmin #maximale veränderung zwischen zwei perioden
    prdmaxdiff = prdmax-prdmin #dito
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(xstart,ystart)
    x = xstart
    h = (hmin+hmax) / 2 #mit den mittleren werten beginnen
    prd = prdmin #damit es sich möglichst schnell bewegt
    cnt = 0 #der erste sinus ist sonst ganz horizontal
    while x < xend:
        y = getqbezier(x,xstart,ystart,xcp,ycp,xend,yend)
        prd = brownian1(prd,prdmin,prdmax,prdmaxdiff)
        h = brownian1(h,hmin,hmax,hmaxdiff)
        ptarget = x+prd,y
        c1 = x+prd/2,y-h
        c2 = x+prd/2,y+h
        if cnt>0: p.C(*c1,*c2,*ptarget)
        x += prd
        cnt += 1
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

def quasitr(xstart=10,y=20,xend=100,siz=10,hmin=3,hmax=5,prdmin=2,prdmax=3,swfac=.5,c='black',**args):
    """quasi triller mit variabler höhe (hmin,hmax) und variabler periode (prdmin,prdmax).
    stroke_width = swfac * ((hmin+hmax)/2) * 0.25
    x,y ist links mitte
    das könnte man durch brownian o.ä. statt uniform noch schöner machen"""
    from random import uniform
    x = xstart
    sw = swfac * ((hmin+hmax)/2) * 0.25
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    p.M(x,y)
    prd = (prdmin+prdmax) / 2
    h = (hmin+hmax) / 2
    while x <= xend-prd:
        x0 = x
        xc1 = x+prd
        xc2 = x+prd
        x += prd*2
        yc1 = y-h
        yc2 = y+h
        p.C(xc1,yc1,xc2,yc2,x,y)
        prd = uniform(prdmin,prdmax)
        h = uniform(hmin,hmax)
    d.append(p)



