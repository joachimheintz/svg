def sharp(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=2/3,arrow=0):
    """sharp sign before a note
    x_note and y_note are the middle of the note
    x_offset_mult: x offset between sharp and note as ratio of y_space"""
    width = y_space*1/2
    x_offset = y_space*x_offset_mult
    ybot = y_note+y_space
    ybot1 = y_note+y_space*1/2 #left
    ybot2 = y_note+y_space*1/9 #right
    ytop = y_note-y_space
    ytop2 = y_note-y_space*1/2 #left
    ytop1 = y_note-y_space*1/9 #right
    x1 = x_note-x_offset-width-y_space/2 #left
    x2 = x_note-x_offset-y_space/2 #right
    xmin = x1-y_space*1/5
    xmax = x2+y_space*1/5
    g = dw.Group(stroke=color,stroke_width=sw)
    g.append(dw.Line(x1,ybot,x1,ytop))
    g.append(dw.Line(x2,ybot,x2,ytop))
    g.append(dw.Line(xmin,ybot1,xmax,ybot2))
    g.append(dw.Line(xmin,ytop1,xmax,ytop2))
    p = dw.Path(stroke=color,stroke_width=sw,fill='none')
    if arrow != 0:
        arryadd = y_space*2/3
        arrxydev = y_space/3
        if arrow == 1:
            ytopright = ytop
            xright = x2
            ytoptop = ytopright-arryadd
            p.M(xright,ytopright)
            p.L(xright,ytoptop)
            p.L(xright-arrxydev,ytoptop+arrxydev)
            p.M(xright,ytoptop)
            p.L(xright+arrxydev,ytoptop+arrxydev)
        if arrow == -1:
            ybotleft = ybot
            xleft = x1
            ybotbot = ybotleft+arryadd
            p.M(xleft,ybotleft)
            p.L(xleft,ybotbot)
            p.L(xleft-arrxydev,ybotbot-arrxydev)
            p.M(xleft,ybotbot)
            p.L(xleft+arrxydev,ybotbot-arrxydev)
    d.append(g)
    d.append(p)

def bflat(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=1,arrow=0):
    """b flat sign before a note
    x_note and y_note are the middle of the note
    x_offset_mult: x offset between sharp and note as ratio of y_space
    arrow: 1=upwards, -1=downwards, 0=none"""
    width = y_space*1/2
    x_offset = y_space*x_offset_mult
    x_left = x_note-x_offset-width
    y_top = y_note-y_space*5/3
    y_bot = y_note+y_space*0.5
    y_end = y_note-y_space*1/4
    p = dw.Path(fill='none',stroke=color,stroke_width=sw)
    p.M(x_left,y_top)
    p.V(y_bot)
    p.Q(x_note-x_offset*1/4,y_note-y_space*3/4 ,x_left,y_end)
    if arrow != 0:
        arr_width = y_space/3
        arr_height = arr_width
        x_arr_left = x_left-arr_width
        x_arr_right = x_left+arr_width
        if arrow == 1:
            p.M(x_left,y_top)
            p.L(x_arr_left,y_top+arr_height)
            p.M(x_left,y_top)
            p.L(x_arr_right,y_top+arr_height)
        if arrow == -1:
            y_botbot = y_bot+y_space
            p.M(x_left,y_bot)
            p.L(x_left,y_botbot)
            p.L(x_arr_left,y_botbot-arr_height)
            p.M(x_left,y_botbot)
            p.L(x_arr_right,y_botbot-arr_height)
    d.append(p)

def natural(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=1,arrow=0):
    """natural sign before a note
    x_note and y_note are the middle of the note
    x_offset_mult: x offset between natural and note as ratio of y_space"""
    width = y_space*2/3
    x_offset = y_space*x_offset_mult
    ytopleft = y_note-y_space*4/3
    ybotleft = y_note+y_space/2
    ytopright = y_note-y_space/2
    ybotright = y_note+y_space*4/3
    xleft = x_note-x_offset-width
    xright = x_note-x_offset
    ydev = y_space/3
    p = dw.Path(stroke=color,stroke_width=sw,fill='none')
    p.M(xleft,ytopleft)
    p.L(xleft,ybotleft)
    p.M(xright,ytopright)
    p.L(xright,ybotright)
    p.M(xleft,ytopright+ydev)
    p.L(xright,ytopright)
    p.M(xleft,ybotleft)
    p.L(xright,ybotleft-ydev)
    if arrow != 0:
        arryadd = y_space/3
        arrxydev = y_space/3
        if arrow == 1:
            ytoptop = ytopleft-arryadd
            p.M(xleft,ytopleft)
            p.L(xleft,ytoptop)
            p.L(xleft-arrxydev,ytoptop+arrxydev)
            p.M(xleft,ytoptop)
            p.L(xleft+arrxydev,ytoptop+arrxydev)
        if arrow == -1:
            ybotbot = ybotright+arryadd
            p.M(xright,ybotright)
            p.L(xright,ybotbot)
            p.L(xright-arrxydev,ybotbot-arrxydev)
            p.M(xright,ybotbot)
            p.L(xright+arrxydev,ybotbot-arrxydev)
    d.append(p)

