def note(x=10,y=10,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    """note with xy as center
    for color: fill='gray' or fill='#444'"""
    sw = y_space * swfac * 0.1 
    r = y_space/2
    p = dw.Path(stroke_width=sw,stroke=c,**args)
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2

def not1tel(x=10,y=10,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    """ganze note"""
    sw = y_space * swfac * 0.2
    r = y_space/2
    p = dw.Path(stroke_width=sw,stroke=c,fill='none',**args)
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2

def notbrevis(x=10,y=10,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1,swlinesfac=1,**args):
    """brevis als ganze note mit strichen
    swlinesfac ist die dicke der vertikalen linien als verhältnis zu sw"""
    sw = y_space * swfac * 0.2
    swlines = sw * 0.5 * swlinesfac
    r = y_space/2
    p = dw.Path(stroke_width=sw,stroke=c,fill='none',**args)
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    xleft = x-r*1.65
    xright = x+r*1.65
    ytop = y-r*1.4
    ybot = y+r*1.4
    d.append(dw.Line(xleft,ytop,xleft,ybot,stroke=c,stroke_width=swlines))
    d.append(dw.Line(xright,ytop,xright,ybot,stroke=c,stroke_width=swlines))
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2

def not2tel(x=20,y=30,dirlen=1,y_space=10,swfac=1,swfac_head=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    """half note with xy as center
    dirlen=1 means in normal length (y_space*2.4) upwards
    dirlen=-1.1 means in length 2.64*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swfac_head is stroke width of the head line, as relation to the line * 1.5
    **args go to the head
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)
    returns the x,y of end of the line to use in 8th notes etc"""
    sw = y_space * swfac * 0.1 
    swhead = sw*swfac_head*1.5
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(stroke=c,fill='none',stroke_width=swhead,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: 
        endxy = p2[0],p2[1]-dirlen*y_space*2.4
        d.append(dw.Line(*p2,*endxy,stroke=c,stroke_width=sw))
    else: 
        endxy = p1[0],p1[1]-dirlen*y_space*2.4
        d.append(dw.Line(*p1,*endxy,stroke=c,stroke_width=sw))
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2
    return endxy

def not4tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,dotted=0,c='#444',
            dotspace=1,dotsiz=1,cline='black',alsvorschlag=False,**args):
    """4ter note with xy as center
    dirlen=1 means in normal length (y_space*2.5) upwards
    dirlen=-1.1 means in length 2.75*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    **args go to the head
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)
    returns the x,y of end of the line to use in 8th notes etc"""
    sw = y_space * swfac * 0.1
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: 
        endxy = p2[0],p2[1]-dirlen*y_space*2.5
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*endxy,stroke=cline,stroke_width=sw))
        if alsvorschlag: d.append(dw.Line(x,y-y_space,x+y_space*1.5,endxy[1],stroke=cline,stroke_width=sw))
    else: 
        endxy = p1[0],p1[1]-dirlen*y_space*2.5
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*endxy,stroke=cline,stroke_width=sw))
        if alsvorschlag: d.append(dw.Line(x+y_space/2,endxy[1],x-y_space*1.2,y+y_space,stroke=cline,stroke_width=sw))
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2
    return endxy

def not8tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,c='#444',
            dotspace=1,dotsiz=1,cline='black',alsvorschlag=False,**args):
    """8th note with xy as center
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    wenn alsvorschlag=True wird strich durchgezogen
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*2.75,
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x,y-y_space,x+y_space*1.5,ptop[1],stroke=cline,stroke_width=sw))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*2.75
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x+y_space/2,pbottom[1],x-y_space*1.2,y+y_space,stroke=cline,stroke_width=sw))
        return pbottom

def not16tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,swflagfac=1,dotted=0,c='#444',
             dotspace=1,dotsiz=1,cline='black',alsvorschlag=False,**args):
    """16th note with xy as center
    dirlen=1 means in normal length (y_space*3) upwards
    dirlen=-1.1 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space*0.2
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    wenn alsvorschlag=True wird strich durchgezogen
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac * 0.2
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*3
        ptop2 = p2[0],ptop[1]+swflag*4
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x,y-y_space,x+y_space*1.5,ptop[1],stroke=cline,stroke_width=sw))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*3
        pbottom2 = p1[0],pbottom[1]-swflag*4
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x+y_space/2,pbottom[1],x-y_space*1.2,y+y_space,stroke=cline,stroke_width=sw))
        return pbottom

def not32tel(x=10,y=10,dirlen=1,y_space=10,swfac=1,swflagfac=1,dotted=0,c='#444',
             dotspace=1,dotsiz=1,cline='black',alsvorschlag=False,**args):
    """32th note with xy as center
    dirlen=1 means in normal length (y_space*3.25) upwards
    dirlen=-1.2 means in length 3.9*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space*0.2
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    wenn alsvorschlag=True wird strich durchgezogen
    **args go to the head
    return top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac * 0.2
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2
    if dirlen > 0: 
        ptop = p2[0],p2[1]-dirlen*y_space*3.25
        ptop2 = p2[0],ptop[1]+swflag*3
        ptop3 = p2[0],ptop2[1]+swflag*3
        d.append(dw.Line(p2[0],p2[1]+y_space/5,*ptop,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*ptop3,ptop3[0]+dxflag,ptop3[1]+dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x,y-y_space,x+y_space*1.5,ptop[1],stroke=cline,stroke_width=sw))
        return ptop
    else:
        pbottom = p1[0],p1[1]-dirlen*y_space*3.25
        pbottom2 = p1[0],pbottom[1]-swflag*3
        pbottom3 = p1[0],pbottom2[1]-swflag*3
        d.append(dw.Line(p1[0],p1[1]-y_space/5,*pbottom,stroke=cline,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=cline,stroke_width=swflag))
        d.append(dw.Line(*pbottom3,pbottom3[0]+dxflag,pbottom3[1]-dyflag,stroke=cline,stroke_width=swflag))
        if alsvorschlag: d.append(dw.Line(x+y_space/2,pbottom[1],x-y_space*1.2,y+y_space,stroke=cline,stroke_width=sw))
        return pbottom

def gruppe(notlist=[10,60,40,50,60,120],
           balken=1, dotlist=0,
           balkdick=1, balkspace=1, balklen=1,
           dirlen=1.5, y_space=10, swfac=1, swfac_head=1, c='#444', dotspace=1, dotsiz=1, fill=True,
           cp_x=0.5, cp_y_shift=0, resolution=100, cline='black', **args):
    """eine gruppe von noten unter einem oder mehreren balken.
        der balken wird als quadratische bezierkurve gezogen; der kontrollpunkt kann
        mit cp_x und cp_y_shift modifiziert werden.
    INPUT:
    notlist: liste mit x,y werten der einzelnen noten
    balken: entweder zahl für die anzahl der balken
        oder liste: wie viele balken bei jeder note (negativ = nach links)
    dotlist: entweder zahl (default 0 = keine)
        oder liste mit zahlen für punktierung jeder einzelnen note 
    balkdick: dicke der balken als relation zum y_space (1 = y_space/3)
    balkspace: abstand zwischen zwei balken als relation zur dicke (1 = dicke*2)
        entweder zahl oder liste für jede note
    balklen: länge eines einzelbalkens als relation zu y_space (1 = y-space/2)
    dirlen: wie bei not4tel; gilt für die randnoten
    cp_x: horizontale position des kontrollpunkte zwischen 0=links und 1=rechts
        default = 0.5 (mitte)
    cp_y_shift: y-verschiebung des kontrollpunkts, als faktor von abs(dirlen)
        default ist 0, dh der kontrollpunkt liegt auf der linie zwischen den beiden randnoten.
        cp_y_shift = 1 würde den kontrollpunkt um dirlen nach oben verschieben
        cp_y_shift = -1 entsprechend nach unten
    resolution: wieviele punkte für die balken (werden dann durch kleine linien verbunden)
    die übrigen parameter sind wie bei note
    fill kann True sein (dann noten gefüllt mit color), oder False (dann hohl)
    gibt x und y von start und ende des äußeren balkens zurück"""
    # input und umformungen
    sw = y_space * swfac * 0.1 
    swhead = sw*swfac_head*1.5
    dick = balkdick * y_space/3
    blen = y_space * 0.5 * balklen
    nothals = dirlen * y_space * 2.5
    # x und y shifts am notenkopf
    dir_vz = dirlen / abs(dirlen) # 1 oder -1
    xshift_head = y_space * 0.6 * dir_vz
    yshift_head = -y_space * 0.3 * dir_vz
    # balken start und ende berechnen
    xstart,ystart = notlist[0],notlist[1]
    xend,yend = notlist[-2],notlist[-1]
    xstart_balken = xstart + xshift_head
    ystart_balken = ystart + yshift_head - nothals
    xend_balken = xend + xshift_head
    yend_balken = yend + yshift_head - nothals
    # den kontrollpunkt festsetzen
    xcp = xstart_balken + (xend_balken-xstart_balken) * cp_x
    ycp = ystart_balken + (yend_balken-ystart_balken)*cp_x - cp_y_shift * abs(nothals)
    # bezierkurve
    bezier = [xstart_balken,ystart_balken,xcp,ycp,xend_balken,yend_balken]
    # die angaben für balken und dots ggf expandieren
    numnotes = round(len(notlist) / 2)
    if not isinstance(balken,list):
        balken = [balken]*numnotes
    if not isinstance(dotlist,list):
        dotlist = [dotlist]*numnotes
    if not isinstance(balkspace,list):
        bspace = [dick * balkspace * 3]*numnotes
    else:
        bspace = [dick * i * 3 for i in balkspace]
    # iterieren 
    for i in range(numnotes):
        # 1. notenköpfe, ggf punkt(e)
        xkopf,ykopf = notlist[i*2],notlist[i*2+1]
        if fill: f = c
        else: f = 'none'
        dt = dotlist[i]
        note(xkopf,ykopf,y_space,swfac=swhead,dotted=dt,c=c,dotspace=dotspace,dotsiz=dotsiz,fill=f,**args)
        # 2. hälse
        xhals = xkopf + xshift_head
        yhals_kopf = ykopf + yshift_head
        yhals_balk = getqbezier(xhals,*bezier)
        d.append(dw.Line(xhals,yhals_kopf,xhals,yhals_balk,stroke=cline,stroke_width=sw))
        # 3. balken
        balk = balken[i] # zahl insgesamt
        val = 1 # mit erstem balken (von oben) beginnen
        # balken zeichnen
        ybalkshift = [0,0]
        while val <= abs(balk):
            #   falls negativ oder letzte note, nach links ziehen
            if balk < 0 or i == numnotes-1: 
                drawqbezier(xhals-blen,xhals,*bezier,sw=dick,c=cline,yshift=ybalkshift)
            #   alles andere nur bis zur vorletzten note
            if i < numnotes-1:
                nextbalk = balken[i+1]
                nexthals = notlist[(i+1)*2] + xshift_head
                res = round((nexthals-xhals)/(xend_balken-xstart_balken) * resolution)
                if res<2: res = 2
                # durchziehen falls nächste note mindestens gleiche anzahl hat
                if abs(nextbalk) >= val: xbalk_ende = nexthals
                # kurzer balken nach rechts wenn balk positiv und nächster kleiner
                elif balk > 0 and val > abs(nextbalk): xbalk_ende = xhals + blen
                # nichts tun wenn vorige note selbe zahl hat und nächste kleiner ist
                else: xbalk_ende = xhals
                # zeichnen 
                drawqbezier(xhals,xbalk_ende,*bezier,sw=dick,c=cline,yshift=ybalkshift,resolution=res)
            # werte aktualisieren
            val += 1
            ybalkshift[0] = ybalkshift[0]+bspace[i]*dir_vz
            if i < numnotes-1: ybalkshift[1] = ybalkshift[1]+bspace[i+1]*dir_vz
            else:  ybalkshift[1] = ybalkshift[1]+bspace[i]*dir_vz
    return xstart_balken,ystart_balken,xend_balken,yend_balken


def hals4tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,dotted=0,dotspace=1,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    r = y_space/2
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*2.5,
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+dotspace*y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += dotspace*y_space/2
    return rpoint

def hals8tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,dotspace=1,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*2.75
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+dotspace*y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += dotspace*y_space/2
    return rpoint

def hals16tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,dotspace=1,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*3
        ptop2 = x,ptop[1]+swflag*3
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*3
        pbottom2 = x,pbottom[1]-swflag*3
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+dotspace*y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += dotspace*y_space/2
    return rpoint

def hals32tel(x=50,y=50,dirlen=1,y_space=10,swfac=1,swflagfac=0.2,dotted=0,dotspace=1,c='#444',**args):
    """nur der hals von xy bis dahin was dirlen sagt
    dirlen=1 means in normal length (y_space*2.75) upwards
    dirlen=-1.2 means in length 3.3*yspace downwards
    swfac is stroke width of the line, as relation to y_space*0.1
    swflag is stroke width of the flag, as relation to y_space (default 0.2)
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    returns top or bottom point of the line"""
    sw = y_space * swfac * 0.1
    swflag = y_space * swflagfac
    r = y_space/2
    dxflag = y_space
    dyflag = y_space*1.33*abs(dirlen)
    if dirlen > 0: 
        ptop = x,y-dirlen*y_space*3.25
        ptop2 = x,ptop[1]+swflag*3
        ptop3 = x,ptop2[1]+swflag*3
        d.append(dw.Line(x,y,*ptop,stroke=c,stroke_width=sw))
        d.append(dw.Line(*ptop,ptop[0]+dxflag,ptop[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop2,ptop2[0]+dxflag,ptop2[1]+dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*ptop3,ptop3[0]+dxflag,ptop3[1]+dyflag,stroke=c,stroke_width=swflag))
        yy = y-y_space/2
        rpoint = ptop
    else:
        pbottom = x,y-dirlen*y_space*3.25
        pbottom2 = x,pbottom[1]-swflag*3
        pbottom3 = x,pbottom2[1]-swflag*3
        d.append(dw.Line(x,y,*pbottom,stroke=c,stroke_width=sw))
        d.append(dw.Line(*pbottom,pbottom[0]+dxflag,pbottom[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom2,pbottom2[0]+dxflag,pbottom2[1]-dyflag,stroke=c,stroke_width=swflag))
        d.append(dw.Line(*pbottom3,pbottom3[0]+dxflag,pbottom3[1]-dyflag,stroke=c,stroke_width=swflag))
        yy = y+y_space/2
        rpoint = pbottom
    if dotted > 0:
        xx = x+dotspace*y_space/2
        for i in range(dotted):
            d.append(dw.Circle(xx,yy,y_space/6,fill=c))
            xx += dotspace*y_space/2
    return rpoint


#old definition of quarter note --- keep for compatibility
def viertel(x=10,y=10,dirlen=1,y_space=10,c='#444',sw=1,**args):
    """4ter note with xy as center
    dirlen=1 means in normal length (y_space*2.5) upwards
    dirlen=-1.1 means in length 2.75*yspace downwards
    sw is stroke width of the line
    **args go to the head"""
    r = y_space/2
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
    p = dw.Path(fill=c,**args)
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dirlen > 0: d.append(dw.Line(p2[0],p2[1]+y_space/5,p2[0],p2[1]-dirlen*y_space*2.5,stroke=c,stroke_width=sw))
    else: d.append(dw.Line(p1[0],p1[1]-y_space/5,p1[0],p1[1]-dirlen*y_space*2.5,stroke=c,stroke_width=sw))

def paus4tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """viertel pause (ha!)
    x,y ist in der mitte der glyphe
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= 1.3 # skalierung zur anpassung an die anderen pausen
    p1 = x+y_space*.1,y+y_space*1.2
    p2 = x+y_space/4,y+y_space*.45
    p3 = x-y_space*.1,y-y_space*.15
    p4 = x+y_space/5,y-y_space*.5
    p5 = x-y_space*.0,y-y_space*.9
    c2 = x-y_space/2,y+y_space/4
    c5 = x-y_space*.0,y-y_space*.7
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c2,*p2)
    p.L(*p3).L(*p4)
    p.Q(*c5,*p5)
    d.append(p)
    if dotted > 0:
        x = x+dotspace*y_space*0.66
        y = y
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/8,fill=c))
            x += dotspace*y_space/2

def paus8tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """achtel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*0.8,y-y_space*1.2
    p2 = x+y_space,y-y_space
    p3 = x,y+y_space*1.5
    c1 = x,y-y_space/4
    c2 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.Q(*c2,*p3)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2
    
def paus16tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """sechzehntel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*0.8,y-y_space*1.4 #oben links
    p2 = x+y_space,y-y_space*1.2 #oben rechts
    p3 = x+y_space*.5,y-y_space*.6 #zweites faehnchen rechts
    p4 = x-y_space*.9,y-y_space*.8 #zweites faehnchen links
    p5 = x,y+y_space*1.5 #unten
    c1 = x,y-y_space*.5
    c2 = x,y-y_space*.1
    c3 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1)
    p.Q(*c1,*p2)
    p.L(*p3)
    p.Q(*c2,*p4)
    p.M(*p3)
    p.Q(*c3,*p5)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2

def paus32tel(x=20,y=30,y_space=10,swfac=1,dotted=0,c='#444',dotspace=1,dotsiz=1,**args):
    """32igstel pause
    x ist in der mitte der glyphe
    y ist die mitte eine imaginären liniensystems
    swfac ist das verhältnis der strichdicke zum y_space
    dotted=0 (default) means no dots, dotted=2 means two dots after the note
    dotspace and dotsiz set the distance and the size of the dot(s)"""
    sw = y_space * swfac * 0.15 #hier skalieren
    y_space *= .7 #skalierung zur anpassung an die anderen pausen
    p1 = x-y_space*.7,y-y_space*1.6 #erstes faehnchen links
    p2 = x+y_space,y-y_space*1.4 #erstes rechts
    p3 = x-y_space*.9,y-y_space*1 #zweites faehnchen links
    p4 = x+y_space*.5,y-y_space*.8 #zweites rechts
    p5 = x-y_space*.9,y-y_space*.4 #drittes faehnchen links
    p6 = x+y_space*.3,y-y_space*.3 #drittes rechts
    p7 = x,y+y_space*1.5 #unten
    c1 = x,y-y_space*.9
    c2 = x,y-y_space*.5
    c3 = x,y-y_space*.1
    c4 = x,y
    p = dw.Path(stroke=c,fill='none',stroke_width=sw,**args)
    p.M(*p1).Q(*c1,*p2)
    p.M(*p3).Q(*c2,*p4)
    p.M(*p5).Q(*c3,*p6)
    p.M(*p2).L(*p4).L(*p6)
    p.Q(*c4,*p7)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space*0.5
        y = p2[1]+y_space/2
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/5,fill=c))
            x += dotspace*y_space/2
