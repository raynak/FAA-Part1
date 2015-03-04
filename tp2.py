import numpy as np
import matplotlib.pyplot as plt
import random as ran

def init():
    global t
    global p
    global N
    global x

    print "chargement des donnees"
    t=np.loadtxt("data/t.txt")
    p=np.loadtxt("data/p.txt")
    N=t.size
    x=np.vstack((np.ones((1,N)),t))
    return

def pasT(pas):
   return 0.5/(0.5+pas)

def nextTheta(theta, pas):
    global x
    global N
    global p
    
    return theta + ((pasT(pas)/N)* np.dot(x,(p - np.dot(x.T, theta))))

def nextThetaSto(theta, pas, i):
    global x
    global p
    
    return theta + pasT(pas)*(np.dot(x[1][i],(p[i] - np.dot(theta.T,x[1][i]))))

def erreurQuadra(theta):
   global p
   global N
   global x
   
   alpha = p - (np.dot(x.T, theta))

   return (1.0 / N) * np.dot(alpha.T, alpha)


def descenteGrad():
    global resGrad
    global erreurQgrad

    print "calcul de la premiere erreur"
    pas=1
    premier = np.array([0,0])
    second = nextTheta(premier, pas)
    arret = abs(erreurQuadra(second) - erreurQuadra(premier))
    resGrad = []
    erreurQgrad= []

    erreurQgrad.append(erreurQuadra(premier))
    erreurQgrad.append(erreurQuadra(second))
    resGrad.append(premier)
    resGrad.append(second)

    print "condition d'arret 1/100000.0 * la difference des deux premiere erreur"
    while arret/100000.0 < abs(erreurQuadra(second) - erreurQuadra(premier)):
       pas = pas+1
       premier=second
       second=nextTheta(premier, pas)
       resGrad.append(second)
       erreurQgrad.append(erreurQuadra(second))

    print "pas sto"
    print pas
    print "abs(arret)/1000.0: {0}".format(arret/100000.0)
    print "abs(Quadra(second) - Quadra(premier)): {0}".format(abs(erreurQuadra(second) - erreurQuadra(premier)))
    print "erreurQuadra {0}".format(erreurQuadra(second))
    return second

def descenteGradSto():
    global resGradSto
    global erreurQgradSto
    global N
    
    ran.seed()
    

    "calcul de la premiere erreur, choix de point aleatoire"
    
    pas=1
    premier = np.array([0,0])
    second = nextThetaSto(premier, pas, ran.randint(0,N-1))
    arret = abs(erreurQuadra(second) - erreurQuadra(premier))
    resGradSto = []
    erreurQgradSto= []
    
    erreurQgradSto.append(erreurQuadra(premier))
    erreurQgradSto.append(erreurQuadra(second))
    resGradSto.append(premier)
    resGradSto.append(second)

    print "condition d'arret 1/100000.0 * la difference des deux premiere erreur"
    while arret/100000.0 < abs(erreurQuadra(second) - erreurQuadra(premier)):
        pas = pas+1
        premier=second
        second=nextThetaSto(premier, pas, ran.randint(0,N-1))
        resGradSto.append(second)
        erreurQgradSto.append(erreurQuadra(second))

    print "sto"
    print pas
    print "abs(arret)/1000.0: {0}".format(arret/100000.0)
    print "abs(Quadra(second) - Quadra(premier)): {0}".format(abs(erreurQuadra(second) - erreurQuadra(premier)))
    print "erreurQuadra {0}".format(erreurQuadra(second))
    return second

    
     
def fTheta(theta):
   global x

   return np.dot(x.T, theta)




def main():
    global resGrad
    global resGradSto
    global erreurQgrad
    global erreurQgradSto
    
    init()
    
    plt.xlabel("temps(s)")
    plt.ylabel("position(m)")
    plt.plot(t,p, '*')

    theta = descenteGrad()
    plt.plot(t, fTheta(theta))

    print "\n"
    
    theta = descenteGradSto()
    plt.plot(t, fTheta(theta))
    
    plt.show()
    
