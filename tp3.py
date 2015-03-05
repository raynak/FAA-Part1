import numpy as np
import matplotlib.pyplot as plt

# scenario
# essaye d'apprendre pour degres= i
# calcul l'erreur cross e1
# apprentissage pour degres =i+1
# calculer erreur cross e2
# tant que e1>e2
# return e1

def init():
    global t
    global p
    global N

    t=np.loadtxt("data/x_C3.txt")
    p=np.loadtxt("data/y_C3.txt")
    N=t.size

def polyT(t, degre):
    
    x=np.vstack((np.ones((1,t.size)),t))
    #mettre a la puissance
    for i in range(2,degre):
        x=np.vstack((x, np.power(t,i)))

    return x

def theta(p, x):
    return np.dot(np.linalg.inv(np.dot(x,x.T)), np.dot(x,p))

def fTheta(x, theta):
    return np.dot(x.T, theta)

#calcul de l'erreur quadratique moyenne
def erreurQuadra(p,x,theta):
   global N

   alpha = p - (np.dot(x.T, theta))

   return (1.0 / N) * np.dot(alpha.T, alpha)

#trace de graph
def trace(y):
   global t
   global p

   plt.plot(t,p, '*')
   plt.plot(t, y, '.')
   plt.xlabel("temps")
   plt.ylabel("position")
   plt.title("Tp3:")
   plt.grid(True)
   plt.show()

def initKFold(i):
    global Tbis
    global Pbis

    Tbis=np.delete(t, [i])
    Pbis=np.delete(p, [i])
    return

def main():
    global t
    global p
    global N

    global Tbis
    global Pbis
    
    init()
    print"ajout du premier polynome"
    Best=0.0
    Temp=0.0
    j=1
    for i in range(2,N):
        initKFold(i);
        Testx= polyT(Tbis,j)
        y=theta(Pbis, Testx)
        #f=fTheta(x,y)
        Best = erreurQuadra(p[i],t[i],y)+ Best
    Best=Best/N-1
    j=j+1

    print"augmentation degre polynome jusqu'a degradation"
    while True:
        for i in range(2,N):
            initKFold(i);
            Testx= polyT(Tbis,j)
            y=theta(Pbis, Testx)
            Temp = erreurQuadra(p[i],t[i],y)+ Temp

        Temp=Temp/N-1
        print "erreur = {0} pour degres {1}".format(Temp, j)
        if(Best>Temp):
            print 'Stop degradation'
            break
        Best=Temp
        Temp=0.0
        j=j+1
    
    print Best
    x=polyT(t,j-1)
    y=theta(p, x)
    f=fTheta(x,y)

    trace(f)
