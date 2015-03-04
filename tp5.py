#tp5 reseaux de Neurones et classificateur naif de bayes
import numpy as np
import cv2

#chargement donnees et autre
def init():
    global a
    global b
    global c
    global ao
    global bo
    global co

    a=np.loadtxt("data/a_1.txt")
    b=np.loadtxt("data/b_1.txt")
    c=np.loadtxt("data/c_1.txt")


    blank = 0*np.ones(len(a),'float')
    ao = np.hstack((np.ones(len(a),'float'), blank))
    ao = np.hstack((ao,blank))

    blank = 0*np.ones(len(b),'float')
    bo = np.hstack((blank, np.ones(len(b),'float')))
    bo = np.hstack((bo,blank))

    blank = 0*np.ones(len(c),'float')
    co = np.hstack((blank, blank))
    co = np.hstack((co,np.ones(len(c),'float')))

def learn(ninputs, nhidden, noutput):
    global a
    global b
    global c
    global ao
    global bo
    global co

    global nnet

    print "input {0}, output {1}, couche cache {2}".format(ninputs, noutput, nhidden)
    
    inputs = np.vstack((np.vstack((a,b)),c))
    
    targets= np.vstack((np.vstack((ao,bo)),co)).T
    
    layers = np.array([ninputs, nhidden, noutput])
    nnet = cv2.ANN_MLP(layers)

    # Some parameters for learning.  Step size is the gradient step size
    # for backpropogation.
    step_size = 0.01

    # Momentum can be ignored for this example.
    momentum = 0.0

    # Max steps of training
    nsteps = 10000

    # Error threshold for halting training
    max_err = 0.0001

    # When to stop: whichever comes first, count or error
    condition = cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS

    # Tuple of termination criteria: first condition, then # steps, then
    # error tolerance second and third things are ignored if not implied
    # by condition
    criteria = (condition, nsteps, max_err)

    # params is a dictionary with relevant things for NNet training.
    params = dict( term_crit = criteria,
                                  train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
                                  bp_dw_scale = step_size,
                                  bp_moment_scale = momentum )

    # Train our network
    num_iter = nnet.train(inputs, targets,
                          None, params=params)

    # Create a matrix of predictions
    predictions = np.empty(targets.shape)

    # See how the network did.
    nnet.predict(inputs, predictions)
    
    # Compute sum of squared errors
    sse = np.sum( (targets - predictions)**2 )

    # Compute # correct
    # true_labels = np.argmax( targets, axis=0 )
    # pred_labels = np.argmax( predictions, axis=0 )
    # num_correct = np.sum( true_labels == pred_labels )
    
    print 'somme erreur quadratique:{0}\n'.format(sse)
    return sse
    
#fonction principal lance par faa.py
def main():
    global a
    global b
    global c
    global ao
    global bo
    global co

    global nnet
    
    init()

    #def construction reseau

    print "Minimisation somme erreur quadratique"
    print "le nombre de couche cache augmente\n"
    hidden=2
    sse = learn(2,hidden,3)
    hidden = hidden +1

    while True:
        sseTemp = learn(2,hidden,3)
        if sseTemp < sse:
            sse=sseTemp
            hidden = hidden +1
        else:
            print '\nStop'
            print 'meilleure sommes des erreur quadratique = {0}'.format(sse)
            print 'Couche cache {0}'.format(hidden-1)
            break
            
