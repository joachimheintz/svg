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

