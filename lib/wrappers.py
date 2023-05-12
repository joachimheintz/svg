def text(txt='',x=10,y=10,fontsize=14,**args):
    """wrapper for d.append(dw.Text(...))
    with fontsize set to 14 as default"""
    d.append(dw.Text(txt,fontsize,x,y,**args))
    
def line(x1=10,y1=10,x2=100,y2=100,c='black',**args):
    """wrapper for d.append(dw.Line(...))
    with c (color) = black as default"""
    d.append(dw.Line(x1,y1,x2,y2,stroke=c,**args))

def rect(x=10,y=10,w=100,h=50,**args):
    """wrapper for d.append(dw.Rectangle(...))"""
    d.append(dw.Rectangle(x,y,w,h,**args))

def dot(x=10,y=10,r=3,c='black',**args):
    """quasi d.append(dw.Circle(...))
    with radius=3 and color=black as default"""
    d.append(dw.Circle(x,y,r,fill=c,**args))

def circ(x=10,y=10,r=3,c='black',swfac=1,**args):
    """quasi d.append(dw.Circle(...))
    with radius=3 and color=black as default
    stroke-width = swfac*r/10"""
    sw = swfac * r / 10
    d.append(dw.Circle(x,y,r,stroke=c,stroke_width=sw,**args))

def lines(x1=10,y1=10,*points,c='black',f='none',close=False,**args):
    """wrapper for d.append(dw.Lines(...))
    with c (color) = black and
    fill (f) = none as default"""
    d.append(dw.Lines(x1,y1,*points,close=close,stroke=c,fill=f,**args))

def path_segq(xyseg=[10,10,30,50,50,20,80,0,100,10],c='black',sw=1,f='none',**args):
    """quasi path mit qbezier als segmente von 
    punkt, kontrollpunkt, ... punkt"""
    p = dw.Path(stroke=c,stroke_width=sw,fill=f,**args)
    p.M(xyseg[0],xyseg[1])
    indx = 2
    while indx+3 < len(xyseg):
        p.Q(xyseg[indx],xyseg[indx+1],xyseg[indx+2],xyseg[indx+3])
        indx += 4
    d.append(p)

def path_segc(xyseg=[10,10,20,10,30,50,50,20, 60,20,80,0,100,10],c='black',sw=1,f='none',**args):
    """quasi path mit cubic bezier als segmente von 
    punkt, cp1, cp2, ... punkt"""
    p = dw.Path(stroke=c,stroke_width=sw,fill=f,**args)
    p.M(xyseg[0],xyseg[1])
    indx = 2
    while indx+5 < len(xyseg):
        p.C(xyseg[indx],xyseg[indx+1],xyseg[indx+2],xyseg[indx+3],xyseg[indx+4],xyseg[indx+5])
        indx += 6
    d.append(p)
