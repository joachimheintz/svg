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
    
def lines(x1=10,y1=10,*points,c='black',f='none',close=False,**args):
    """wrapper for d.append(dw.Lines(...))
    with c (color) = black and
    fill (f) = none as default"""
    d.append(dw.Lines(x1,y1,*points,close=close,stroke=c,fill=f,**args))
