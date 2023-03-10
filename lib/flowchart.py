# source for draw2Svg: https://github.com/aufarah/draw2Svg
# doc: https://github.com/joachimheintz/draw2SvgDocs

#import draw2Svg as dw
#wdth,hght = 500,800
#d = dw.Drawing(wdth,hght)


def vert_arrow(x,y1,y2,w=8):
    p = dw.Path(stroke='black',fill='none')
    p.M(x,y1)
    p.V(y2)
    p.M(x-w,y2-w)
    p.L(x,y2+1)
    p.L(x+w,y2-w)
    return p

def osc(x_mid,y_mid,r=70,text='poscil',textsize=20):
    y_top = y_mid-r/2
    d.append(dw.Pie(x_mid,y_top,r,0,180,fill='none',stroke='black'))
    d.append(dw.Text(text,textsize,x_mid,y_mid,
                 text_anchor='middle',style='font-family: courier',stroke='black'))
    x_in_left = x_mid-r/2
    x_in_right = x_mid+r/2
    y_out = y_mid+r/2
    return ((x_in_left,y_top),(x_in_right,y_top),(x_mid,y_out))

def linseg(x_mid,y_mid,w=100,h=40,text='linseg',textsize=20):
    y_top = y_mid-h/2
    d.append(dw.Rectangle(x_mid-w/2,y_top,w,h,stroke='black',fill='none'))
    d.append(dw.Text(text,textsize,x_mid,y_mid-textsize/4,valign='middle',
                 text_anchor='middle',style='font-family: courier',stroke='black'))
    y_out = y_mid+h/2
    x_in_left = x_mid-w/3
    x_in_right = x_mid+w/3
    return ((x_in_left,y_top),(x_mid,y_top),(x_in_right,y_top),(x_mid,y_out))

def linen(x_mid,y_mid,w=160,h=40,text='linen',textsize=20):
    y_top = y_mid-h/2
    d.append(dw.Rectangle(x_mid-w/2,y_top,w,h,stroke='black',fill='none'))
    d.append(dw.Text(text,textsize,x_mid,y_mid-textsize/4,valign='middle',
                 text_anchor='middle',style='font-family: courier',stroke='black'))
    y_out = y_mid+h/2
    x_left = x_mid-w/2
    x_in_1 = x_left + w*.15
    x_in_2 = x_left + w*.5
    x_in_3 = x_left + w*.7
    x_in_4 = x_left + w*.9
    return ((x_in_1,y_top),(x_in_2,y_top),(x_in_3,y_top),(x_in_4,y_top),(x_mid,y_out))

def converter(x_mid,y_mid,w=100,h=40,text='converter',textsize=20):
    y_top = y_mid-h/2
    d.append(dw.Rectangle(x_mid-w/2,y_top,w,h,stroke='black',fill='none'))
    d.append(dw.Text(text,textsize,x_mid,y_mid-textsize/4,valign='middle',
                 text_anchor='middle',style='font-family: courier',stroke='black'))
    y_out = y_mid+h/2
    x_in = x_mid
    x_out = x_mid
    return ((x_in,y_top),(x_out,y_out))    

def outall(x_mid,y_mid,r=40,text='outall',textsize=20):
    d.append(dw.Circle(x_mid,y_mid,r,stroke='black',fill='none'))
    d.append(dw.Text(text,textsize,x_mid,y_mid-textsize/4,text_anchor='middle',
                     valign='middle',style='font-family: courier',stroke='black'))
    return (x_mid,y_mid-r)

def input(x,y,len=10):
    d.append(dw.Line(x,y,x,y-len,stroke='black'))
    return(x,y-len)

def connect(x1,y1,x2,y2,from_top=0.4):
    """x1,y1 is on top"""
    y_dist = y2-y1
    y_mid = y1 + y_dist*from_top
    p = dw.Path(stroke='black',fill='none')
    p.M(x1,y1)
    p.V(y_mid)
    p.H(x2)
    p.L(x2,y2)
    d.append(p)
    return y_mid

def connect2var(x1,y1,x2,y2,sweep=1,from_top=0.4,arcrad=10):
    """connects to or from a variable name
    x1,y1 is on top"""
    y_dist = y2-y1
    if sweep==1: y2_line = y2-arcrad
    else: y2_line = y2+arcrad
    y_mid = y1 + y_dist*from_top
    p = dw.Path(stroke='black',fill='none')
    p.M(x1,y1)
    p.V(y_mid)
    p.H(x2)
    p.L(x2,y2_line)
    p.M(x2-arcrad,y2)
    p.A(arcrad,arcrad,0,0,sweep,x2+arcrad,y2)
    d.append(p)
    return y_mid

# the following is left for backwards compatibility
# better use xgrid and ygrid
def grid(num,length=800,margin_1=40,margin_2=41):
    """returns a list of num grid values between
    margin_1 and height-margin_2 which are subtracted from length.
    for horizontal, it counts from left to right
    for vertical, it counts from top to bottom"""
    real_length = length - margin_1 - margin_2
    grid_step = real_length / (num-1)
    return [i*grid_step+margin_1 for i in range(num)]

def tick(x,y,leng=-5,color='black',**args):
    """axes tick
    leng negative means from x,y to left
    leng positive means to bottom"""
    if leng<0: d.append(dw.Line(x,y,x+leng,y,stroke=color,**args))
    else: d.append(dw.Line(x,y,x,y+leng,stroke=color,**args))


