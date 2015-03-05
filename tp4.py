import numpy as np
import matplotlib.pyplot as plt

#iniit des donnees
def init():
    global data
    global Pfemme
    global Phomme
    
    
    f=np.loadtxt("data/taillepoids_f.txt")
    h=np.loadtxt("data/taillepoids_h.txt")
    Nf=f.size
    Nh=h.size

    Pfemme=(Nf)/(Nf+Nh)
    Phomme=(Nh)/(Nf+Nh)
    
    f=np.vstack((np.ones((1,Nf/2)),f.T))
    h=np.vstack(((np.ones((1,Nh/2))*0),h.T))

    data=np.concatenate((f,h),axis=1)
    
# function qui pour un x donne retourne la valeur y
# x appartient au donnees
def oracle(x):
    global data
    return data[0,x]

def fTheta(theta):
    global data
    return np.dot(theta.T, data)
    # return np.dot(data.T, theta)

def sigmoide(t, A, b):
    return (1.0/(1.0+np.exp(-((A*t)+b))))

def sigmoideF(theta):
    print fTheta(theta)
    return (1.0/(1.0+np.exp(-fTheta(theta))))

def sigmoideThetaTransposeX(theta, x):
    return sigmoide(x, theta, fTheta)

def pasT(pas):
    return 0.5/(0.5+pas)

def nextTheta(theta, pas):
    global data
    quartCal=np.dot(data,(data[0] - np.sum(np.dot(data.T, theta))))
    demiCal=(pasT(pas)/data[0].size)* quartCal
    
    return theta + demiCal

def erreurQuadra(theta):
    global data
    alpha = data[0] - (np.dot(data.T, theta))
    return (1.0 / data.size) * np.dot(alpha.T, alpha)


def descenteGrad(theta0):
    global resGrad
    global erreurQgrad
    global resGradSto
    global erreurQgradSto

    pas=1
    premier = theta0
    second = nextTheta(premier, pas)
    arret = abs(erreurQuadra(second) - erreurQuadra(premier))
    resGrad = []
    erreurQgrad= []

    erreurQgrad.append(erreurQuadra(premier))
    erreurQgrad.append(erreurQuadra(second))
    resGrad.append(premier)
    resGrad.append(second)
    
    while arret/10000.0 < abs(erreurQuadra(second) - erreurQuadra(premier)):
        
        pas = pas+1
        premier=second
        second=nextTheta(premier, pas)
        resGrad.append(second)
        erreurQgrad.append(erreurQuadra(second))

        print "pas"
        print pas
        print "abs(arret)/1000.0: {0}".format(arret/100000.0)
        #print "abs(Quadra(second) - Quadra(premier)): {0}".format(abs(erreurQuadra(second) - erreurQuadra(premier)))
        print "erreurQuadra {0}".format(erreurQuadra(second))
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

   # taille = sys.argv[1:]
   #poids = sys.arg[2:]
   #donnee = np.array([taille, poids])

    #init
    init()
    theta0=np.array([0,0,0])
    theta=descenteGrad(theta0)
    
    plt.plot(sigmoideF(theta), '*')

    #plt.plot(data[1], sigmoide(data[1],1,-170),'*')
    plt.show()
