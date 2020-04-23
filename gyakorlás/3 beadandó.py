def tortosszeadas (sz1,n1,sz2,n2):
    lkkt=n1*n2//lnko(n1,n2)
    sz1=sz1*lkkt//n1
    sz2=sz2*lkkt//n2
    tortszamlalo=sz1+sz2
    egyszerusites=lnko(tortszamlalo,lkkt)
    return "{}/{}".format(tortszamlalo//egyszerusites,lkkt//egyszerusites)


def lnko(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(tortosszeadas(12,66,22,77))