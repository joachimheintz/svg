# import drawsvg as dw
#w,h = 842,595
#d = dw.Drawing(w,h)

def showGridOnMargins(textsiz=10):
    """make sure that xnum etc are defined globally"""
    for i in range(xnum):
        text('%d'%i,xgrid(i),0,textsiz,text_anchor='middle',valign='top')
        text('%d'%i,xgrid(i),h,textsiz,text_anchor='middle')
    for i in range(ynum):
        text('%d'%i,0,ygrid(i),textsiz,valign='middle')
        text('%d'%i,w,ygrid(i),textsiz,text_anchor='end',valign='middle')

def showWritingSpace():
    """uses global vars"""
    d.append(dw.Rectangle(mleft,mtop,xsize,ysize,stroke='black',fill='none',stroke_opacity=0.2))
