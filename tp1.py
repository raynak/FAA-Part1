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
   global th

   print("Calcul de  f(theta) par la formule : XTranspote Theta")
   return np.dot(x.T, th)


#calcul de l'erreur quadratique moyenne
def erreurQuadratique():
   global p
   global N
   global x
   global th

   alpha = p - (np.dot(x.T, th))
   print "Calcul de l'erreur quadratique par la formule : (1/N)( (Y-(XT*Theta))T )*(Y-(XT*Theta)) )\n"
   return (1.0 / N) * np.dot(alpha.T, alpha)


#trace de graph
def trace(fth):
   global t
   global p

   plt.plot(t,p, '*')
   plt.plot(t, fth)
   plt.xlabel("temps")
   plt.ylabel("position")
   plt.title("Tp1: Prediction de trajectoires par regression lineaire")
   plt.grid(True)
   plt.show()
   

#if __name__ == '__main__':
def main():
   global t
   global p
   global x
   global th
   global fth
   
   print "Deroulement des calculs"
   th= theta()
   fTh= fTheta()
   erreurQuadra = erreurQuadratique()

   print "theta {0} \nftheta {1} \nerreurQuadra {2}".format(th, fTh, erreurQuadra)
   trace(fTh)
