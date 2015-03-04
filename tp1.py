import numpy as np
import matplotlib.pyplot as plt

#theta() permet d'extraire de t et p theta
#ou theta=(XX.t)^-1 (XY)
def theta():

   global x
   global t
   global p
   global N
   
   t= np.loadtxt("data/t.txt")
   p= np.loadtxt("data/p.txt")

   N = t.size

   un= np.ones((1,N))

   x= np.vstack((un,t))

   print "Calcul de Theta par la formule :  ( (X * XT)^-1 * (Y * X ) )"
   return np.dot(np.linalg.inv(np.dot(x,x.T)), np.dot(x,p))


# f(theta)=(1/N)(Y-x.T theta)^2
def fTheta():

   global x
   global theta

   print("Calcul de  f(theta) par la formule : XTranspote Theta")
   return np.dot(x.T, theta)


#calcul de l'erreur quadratique moyenne
def erreurQuadra():
   global p
   global N
   global x

   alpha = p - (np.dot(x.T, theta))
   print "Calcul de l'erreur quadratique par la formule : (1/N)( (Y-(XT*Theta))T )*(Y-(XT*Theta)) )\n"
   return (1.0 / N) * np.dot(alpha.T, alpha)


#trace de graph
def trace(ftheta):
   global t
   global p
   global theta

   plt.plot(t,p, '*')
   plt.plot(t, fTheta)
   plt.xlabel("temps")
   plt.ylabel("position")
   plt.title("Tp1: Prediction de trajectoires par regression lineaire")
   plt.grid(True)
   plt.show()
   

if __name__ == '__main__':
   global t
   global p
   global x
   
   print "Deroulement des calculs"
   theta= theta()
   fTheta= fTheta()
   erreurQuadra = erreurQuadra()

   print "theta {0} \nftheta {1} \nerreurQuadra {2}".format(theta, fTheta, erreurQuadra)
   trace(fTheta)
