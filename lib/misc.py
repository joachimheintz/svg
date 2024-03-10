def krachen(xstart=10,ystart=10,xend=100,yend=30,yrange=10,sw=1,c='black',
            lenminmax=(5,10),densminmax=(1,5),**args):
    """kleine krackel für elektronik 120 in bizarre plätze
    schneidet hinten nicht ab, sondern lässt die kleinen krackel auslaufen"""
    from random import uniform
    # länge der einzelnen elemente
    lmin,lmax = lenminmax
    # element pro 10 pixel am anfang und am ende
    densmin,densmax = densminmax
    x = xstart
    p = dw.Path(fill='none',stroke=c,stroke_width=sw,**args)
    while x < xend:
        # wo ist der y mittelpunkt
        y = ystart + (x-xstart) * ((yend-ystart)/(xend-xstart))
        # endpunkt dieses krackels
        xmax = x + uniform(lmin,lmax)
        # welche density hier
        dens = densmin + (x-xstart) * ((densmax-densmin)/(xend-xstart))
        p1 = x,y+uniform(-yrange/2,yrange/2)
        p2 = uniform(x,xmax),y+uniform(-yrange/2,yrange/2)
        p3 = xmax,y+uniform(-yrange/2,yrange/2)
        p.M(*p1)
        p.L(*p2)
        p.L(*p3)
        x += 10 / dens
    d.append(p)

def raute(x=20,y=20,w=5,h=10,c='black',f='black',sw=0,**args):
    """xy ist der mittelpunkt
    w und h die absolute breite und höhe
    wenn hohl, f='none' setzen"""
    p1 = x-w/2,y
    p2 = x,y-h/2
    p3 = x+w/2,y
    p4 = x,y+h/2
    p = dw.Path(stroke=c,stroke_width=sw,fill=f,**args)
    p.M(*p1).L(*p2).L(*p3).L(*p4).L(*p1)
    d.append(p)

def kasten(x=10,y=10,w=25,h=10,c='black',sw=1,**args):
    """macht einen kasten (umrahmung)
    xy sind oben links"""
    d.append(dw.Rectangle(x,y,w,h,stroke=c,stroke_width=sw,fill='none',**args))


