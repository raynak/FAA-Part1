#data a et b

import numpy as np

def init():
    global a
    global b
    global inputs
    global targets

    print "chargement des donnees"
    a=np.loadtxt("data/a.txt")
    b=np.loadtxt("data/b.txt")

    inputs= np.vstack((a,b))
    targets= np.hstack((-1*np.ones(len(a)),np.ones(len(b))))
    
    print targets.shape
    print inputs.shape


def main():
    global a
    global b
    global inputs
    global targets

    ksi=0.5
    
    init()

    t=0
    d=np.empty(inputs.shape)

    for i in range(0, len(d)):
        d[i]=1.0/len(d)

    e=1

    print "t={0},\npour tout i d[i] = {1},\n e={2},".format(t, d[0], e)
    
    while(E > ksi):
        print "entrainement pondere par d"
        

        print "weak hypotheses ht"
        if (t !=0):
            ht=np.vstack((ht,np.empty(output.shape)))
        else:
            ht=np.empty(output.shape)
        

        print "calcul de thetat, somme (ht(xi) != yi) d[i]"
        thetat=0
        for i in range(0,len(targets)):
            if(ht(i) != targets[i]):
                thetat = thetat + d[i]

        print "thetat={0}".format(thetat)
        
        print "calcul de alphaT 1/2 ln((1-thetat)/(thetat))"
        if(t !=0 ):
            tmp= 1.0/2.0 * np.log((1-thetat)/(thetat))
            alphaT=np.vstack((alphaT, np.ones(1, 'float')*tmp))
        else:
            alphaT=np.ones(1, 'float')*1.0/2.0 * np.log((1-thetat)/(thetat))
            
        print "update poids, si il y a une erreur elle est ici update D"
        sommeD=0
        for i in range(0, len(d)):
            sommeD=sommeD+d[i]
        for i in range(0,len(d)):
            d[i]=(d[i]*np.exp(-alphaT[t]*target[i]*ht[t][i]))/(sommeD)

        print "strong hypotheses h(xi)=sign somme sur t alphat ht(xi)"
        h=np.empty(targets.shape)

        for i in range(0,len(targets)):
            tmp=0
            for j in range(0,t):
                tmp= tmp+alphaT[j]*ht[j][i]
            if tmp > 1 :
                h[i]=1
            else:
                h[i]=0
        
        
        print "strong classifier error E=somme(h(xi) != yi) 1/N"
        E=0
        for i in range(0,len(h)):
            if(h(i) != targets[i]):
                E= E + 1.0/len(h)

        print "E={0}".format(E)
        print "t++ {0}".format(t)
