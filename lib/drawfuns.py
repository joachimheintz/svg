#import drawsvg as dw
#wdth,hght = 500,800
#d = dw.Drawing(wdth,hght)

def scale(inval,inmin,inmax,outmin,outmax):
    """scales inval which is between inmin and inmax
    to the range between outmin and outmax"""
    return (inval-inmin)*((outmax-outmin)/(inmax-inmin))+outmin

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

