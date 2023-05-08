#import drawsvg as dw
#wdth,hght = 500,800
#d = dw.Drawing(wdth,hght)

def scale(inval,inmin,inmax,outmin,outmax):
    """scales inval which is between inmin and inmax
    to the range between outmin and outmax"""
    return (inval-inmin)*((outmax-outmin)/(inmax-inmin))+outmin

def yfrompoints(x=45,x1=30,y1=20,x2=60,y2=30):
    """gibt den y wert für x auf der durch die beiden punkte
    x1,y1 und x2,y2 definierten geraden zurück"""
    return y1 + ((y2-y1)/(x2-x1)) * (x-x1)

def yfromsegments(x,xyseg=[10,20,30,20,60,30,70,10]):
    """gibt y für eine kette von (mindestens 2) xy segmenten zurück"""
    indx = 2 # das wären die ersten beiden segmente
    while indx < len(xyseg) and xyseg[indx] < x:
        indx += 2
    if indx >= len(xyseg): indx = len(xyseg)-2
    # nun den y wert berechnen
    x1,y1,x2,y2 = xyseg[indx-2:indx+2]
    return y1 + ((y2-y1)/(x2-x1)) * (x-x1)


def x_accelrit(xstart=10,xend=100,numnotes=10,ratio=3/4,tolerance=1,maxloops=100):
    """mach eine accelerando oder ritardando sequenz von numnotes zwischen xstart und xend.
    der abstand von einer note zur nächsten wird durch ratio gesetzt:
    ratio = 1: alles noten sind gleichmäßig
    ratio < 1: accelerando
    ratio > 1: ritardando
    in bäuerlicher denkweise wird das ganze mit einem annäherungsverfahren gemacht:
    tolerance setzt die akzeptierte abweichung des letzten x-wertes von xend fest
    zur sicherheit setzt maxloops die maximale anzahl der annäherungen fest
    zurückgegeben wird die liste mit numnotes x-werten"""
    # gleichmäßige verteilung als startpunkt
    dist = (xend-xstart) / (numnotes-1)
    # liste initialisieren
    xlis = [xstart]*numnotes
    xlis[1] = xstart+dist
    # vom ersten abstand ausgehen und die anderen noten nach ratio verteilen
    x1 = xlis[1]
    cnt = 0
    while abs(xend-xlis[-1]) > tolerance and cnt < maxloops:
        disthier = x1-xstart
        ds = disthier
        x = xstart
        for i in range(1,numnotes):
            x += ds
            xlis[i] = x
            ds *= ratio    
        # wenn zu weit links, ursprüngliches interval + hälfte
        if xlis[-1] < xend: x1 = xstart + disthier * 1.5
        # wenn zu weit rechts, ursprüngliches interval halbieren
        else: x1 = xstart + disthier * .5
        cnt += 1
    return xlis

def accel_stacc(xlis,ybot,ybotadd=0,dirlen=1,y_space=10,swfac=1,swbalkfac=1,
                c='#444',dotsizfac=1,startbalkindx=1,endbalkindx=-1,**args):
    """macht die accel-staccato figur
    xlis bekommt den output von x_accelrit
    ybotadd ist ein y-shift von ton zu ton
    startbalkindx ist der index in xlis bei dem der zweite balken anfängt"""
    halslen = y_space*dirlen*2.5
    swhals = y_space * swfac * 0.1 
    swbalk = y_space * .3 * swbalkfac
    dotsiz = y_space * .15 * dotsizfac
    ytop = ybot-halslen
    for x in xlis:
        line(x,ytop,x,ybot,stroke_width=swhals)
        dot(x,ybot+4*dotsiz,dotsiz)
        ybot += ybotadd
    line(xlis[0],ytop+swbalk/2,xlis[-1],ytop+swbalk/2,stroke_width=swbalk)
    line(xlis[startbalkindx],ytop+swbalk/2,xlis[endbalkindx],ytop+swbalk/2+swbalk*3,stroke_width=swbalk)

def rit_stacc(xlis,ybot,ybotadd=0,dirlen=1,y_space=10,swfac=1,swbalkfac=1,
                c='#444',dotsizfac=1,endbalkindx=-1,**args):
    """wie accel-staccato aber als rit
    xlis bekommt den output von x_accelrit
    ybotadd ist ein y-shift von ton zu ton
    endbalkindx ist der index in xlis bei dem der zweite balken aufhört"""
    halslen = y_space*dirlen*2.5
    swhals = y_space * swfac * 0.1 
    swbalk = y_space * .3 * swbalkfac
    dotsiz = y_space * .15 * dotsizfac
    ytop = ybot-halslen
    for x in xlis:
        line(x,ytop,x,ybot,stroke_width=swhals)
        dot(x,ybot+4*dotsiz,dotsiz)
        ybot += ybotadd
    line(xlis[0],ytop+swbalk/2,xlis[-1],ytop+swbalk/2,stroke_width=swbalk)
    line(xlis[0],ytop+swbalk/2+swbalk*3,xlis[endbalkindx],ytop+swbalk/2,stroke_width=swbalk)


def getqbezier(x=40,x0=10,y0=10,x1=50,y1=30,x2=100,y2=80):
    """ermittelt den y wert vom punkt x in einer quadratischen bezierkurve
    für x0 (startpunkt) < x1 (kontrollpunkt) < x2 (endpunkt)
    gilt also nur wenn der x-wert des kontrollpunkts zwischen start und ende liegt
    für universelle bezierkurven müsste man die formel noch justieren"""
    t = (x-x0) / (x2-x0) # 0 <= t <= 1 
    y = (1 - t) * (1 - t) * y0 + 2 * (1 - t) * t * y1 + t * t * y2
    return y

def drawqbezier(xstart=10,xend=100,x0=10,y0=10,x1=50,y1=30,x2=100,y2=80,resolution=10,sw=1,c='black',yshift=[0,0],**args):
    """zeichnet die punkte von xstart bis xend in einer quadratischen bezierkurve.
    diese wird durch x0,y0 (start), x1,y1 (kontrollpunkt) und x2,y2 (endpunkt) definiert wird.
    gilt nur für x0 (startpunkt) < x1 (kontrollpunkt) < x2 (endpunkt)
    die kurve wird in resolution punkte zerlegt und als folge kleiner gerader linien gezogen
    (verbesserung: das wiederum als bezier segmente zu machen)
    sw = stroke_width, c = color
    yshift = parallele verschiebung in y-richtung am anfang und am ende (oder zahl = überall gleich)"""
    if not isinstance(yshift,list): yshift = [yshift]*2
    x_segm = (xend-xstart) / (resolution-1)
    yshift_segm = (yshift[1]-yshift[0]) / (resolution-1)
    x = xstart
    t = (x-x0) / (x2-x0) # 0 <= t <= 1 
    y = (1 - t) * (1 - t) * y0 + 2 * (1 - t) * t * y1 + t * t * y2
    for i in range(resolution-1):
        xnext = xstart + (i+1)*x_segm
        t = (xnext-x0) / (x2-x0) # 0 <= t <= 1 
        ynext = (1 - t) * (1 - t) * y0 + 2 * (1 - t) * t * y1 + t * t * y2
        yshift0,yshift1 = yshift[0]+yshift_segm*i,yshift[0]+yshift_segm*(i+1)
        d.append(dw.Line(x,y+yshift0,xnext,ynext+yshift1,stroke=c,stroke_width=sw,**args))
        x = xnext
        y = ynext

def xgrid(inval,off=0):
    """for xnum=4, inval is from 0 (left) to 3 (right)
    as range to write
    off is subtracted from inval"""
    inval -= off
    return scale(inval,0,xnum-1,mleft,mleft+xsize)

def ygrid(inval):
    """for num=11, inval is from 0 (top) to 10 (bottom)
    as range to write"""
    return scale(inval,0,ynum-1,mtop,mtop+ysize)

def vline(x=10,y=10,l=10,c='black',sw=1,**args):
    """vertical line in length l
    positive l is downwards"""
    d.append(dw.Line(x,y,x,y+l,stroke=c,stroke_width=sw,**args))

def hline(x=10,y=10,l=100,c='black',sw=1,**args):
    """horizontal line in length l
    positive l is to right side"""
    d.append(dw.Line(x,y,x+l,y,stroke=c,stroke_width=sw,**args))

def arrow(x=10,y=10,l=30,w=8,rot=0,c='black',sw=1,**args):
    """simple arrow. rot=0 means downwards"""
    y2 = y+l
    p1 = x-w,y2-w
    p2 = x+w,y2-w
    p = dw.Path(stroke_width=sw,stroke=c,fill='none',transform='rotate(%f %f %f)' % (rot,x,y),**args)
    p.M(x,y)
    p.V(y2)
    p.M(*p1)
    p.L(x,y2)
    p.L(*p2)
    d.append(p)

def brownian1(prevValue=10,minValue=10,maxValue=30,maxDev=10,minDev=0):
    """gibt einen zufallswert heraus, der vom vorigen status abhängt.
    maxDev ist die maximal mögliche abweichung (positiv und negativ),
    minDev (normalerweise 0) die minimale abweichung.
    min und max Value sind die grenzen.
    die bewegungsform wird hier als rückprall gesetzt:
    wenn der vorige wert 9 ist und die eigentliche abweichung +3,
    dann wird die abweichung zu -2, landet also bei 8"""
    from random import uniform
    if minValue>maxValue:
        vmin = maxValue
        vmax = minValue
    else:
        vmin = minValue
        vmax = maxValue
    dev = uniform(minDev,maxDev)
    # evt richtung verändern
    if uniform(-1,1) < 0: dev *= -1
    # nun die möglichkeiten
    newVal = prevValue+dev
    if newVal > vmax:
        distToLimit = vmax-prevValue
        Val = vmax - (dev-distToLimit)
    elif newVal < vmin:
        distToLimit = vmin-prevValue
        Val = vmin - (dev-distToLimit)
    else: Val = newVal
    return Val
    
