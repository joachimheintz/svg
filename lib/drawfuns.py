#import drawsvg as dw
#wdth,hght = 500,800
#d = dw.Drawing(wdth,hght)

def scale(inval,inmin,inmax,outmin,outmax):
    """scales inval which is between inmin and inmax
    to the range between outmin and outmax"""
    return (inval-inmin)*((outmax-outmin)/(inmax-inmin))+outmin

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

