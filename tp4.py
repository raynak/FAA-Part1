import numpy as np
import matplotlib.pyplot as plt

#iniit des donnees
def init():
    global data
    global target
    global Pfemme
    global Phomme
    
    
    f=np.loadtxt("data/taillepoids_f.txt")
    h=np.loadtxt("data/taillepoids_h.txt")
    Nf=f.size
    Nh=h.size

    Pfemme=(Nf)/(Nf+Nh)
    Phomme=(Nh)/(Nf+Nh)
    
   # f=np.vstack((np.ones((1,Nf/2)),f.T))
   # h=np.vstack(((np.ones((1,Nh/2))*0),h.T))

    #data=np.concatenate((f,h),axis=1)
    
    data=np.vstack((f,h)).T
 
    target = np.hstack((np.ones((1,Nf/2)),np.ones((1,Nh/2))*0)).T


def fTheta(theta, data):
    print data.shape
    print theta.T
    return np.dot(theta.T, data)
    # return np.dot(data.T, theta)

def sigmoide(t, A, b):
    return (1.0/(1.0+np.exp(-((A*t)+b))))

def sigmoideF(theta, x):
    #print fTheta(theta, x)
    return (1.0/(1.0+np.exp(-fTheta(theta, x))))

def sigmoideThetaTransposeX(theta, x):
    #return sigmoide(x, theta, fTheta)
    return sigmoideF(theta, x)

def pasT(pas):
    return 0.5/(0.5+pas)

def nextTheta(theta, pas):
    global data
 
    quartCal=np.dot(data, target - np.sum(np.dot(data.T, theta)))
    demiCal=(pasT(pas)/target.size)* quartCal
    print quartCal
    return theta + demiCal

def erreurQuadra(theta):
    global data
    global target
    
    print "npdot"
    npdot = np.dot(data.T, theta)
    print "alpha"

    print target.shape
    print npdot.shape
    
    alpha = target - npdot
    
    print "Return de l'erreur quadratique"
    return (1.0 / data.size) * np.dot(alpha.T, alpha)

def risqueEmpirique(theta):
    global data
    global target
    N = data.size/2
    Rn = 0.0
    
    print "Calcul du risque empirique"
    for i in range(data.size):
        logsigmoide = np.log( sigmoideThetaTransposeX(theta, data[i]))
        logUnMoinsSigmoide = np.log( 1 - sigmoideThetaTransposeX(theta, data[i]))
        Rn = Rn + (-target[i] * logsigmoide - (1 - target[i]) * logUnMoinsSigmoide)
    Rn = Rn/N
    return Rn
        


def descenteGrad(theta0):
    #global resGrad
    #global erreurQgrad
    #global resGradSto
    #global erreurQgradSto
    global risqueEmpirique

    print "Descente de gradient"
    pas=1
    premier = theta0
    print "Calcul du premier theta suivant"
    second = nextTheta(premier, pas)
    
    """print "Calcul du cas d'arret"
    print "Calcul de l'erreur quadra seconde"
    erreurQuadraSecond = erreurQuadra(second)
    print "Calcul de l'erreur quadra premiere"
    erreurQuadraPremiere = erreurQuadra(premier)
    arret = abs(erreurQuadraSecond - erreurQuadraPremiere)
    print arret"""
    #resGrad = []
    #erreurQgrad= []

    #erreurQgrad.append(erreurQuadra(premier))
    #erreurQgrad.append(erreurQuadra(second))
    #resGrad.append(premier)
    #resGrad.append(second)
    
    print "Minimisation du risque empirique"
    while risqueEmpirique(second)<risqueEmpirique(premier):
        
        pas = pas+1
        premier=second
        second=nextTheta(premier, pas)

        print "pas"
        print pas
        print "Risque Empirique {0}".format(risqueEmpirique(premier))
    return second


def defineY(x, tau, theta0):
    theta = descenteGrad(theta0)
    sigm = sigmoideF(theta)
    if (sigm >= tau): return 1
    return 0


if __name__ == '__main__':
    global data
    global Pfemme
    global Phomme
    global target

   # taille = sys.argv[1:]
   #poids = sys.arg[2:]
   #donnee = np.array([taille, poids])

    #init
    init()
    theta0=np.array([0,0])
    theta=descenteGrad(theta0)
    
    plt.plot(sigmoideF(theta), '*')

    #plt.plot(data[1], sigmoide(data[1],1,-170),'*')
    plt.show()
