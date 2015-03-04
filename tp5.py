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
                             
#fonction principal lance par faa.py
def main():
    global a
    global b
    global c
    global ao
    global bo
    global co
    init()

    #def construction reseau

    ninputs= 2

    nhidden = 8

    noutput = 3

    print "input {0}, output {1}, couche cache {2}".format(ninputs, noutput, nhidden)
    
    inputs = np.vstack((np.vstack((a,b)),c))

    print inputs
    
    targets= np.vstack((np.vstack((ao,bo)),co)).T

    print "inputs"
    print inputs.shape

    print "target"
    print targets.shape
    
    layers = np.array([ninputs, nhidden, noutput])
    nnet = cv2.ANN_MLP(layers)

    # Train our network
    num_iter = nnet.train(inputs, targets, None)

    # Create a matrix of predictions
    predictions = np.empty(targets.shape)

    # See how the network did.
    nnet.predict(inputs, predictions)
    
    # Compute sum of squared errors
    sse = np.sum( (targets - predictions)**2 )

    # Compute # correct
    true_labels = np.argmax( targets, axis=0 )
    pred_labels = np.argmax( predictions, axis=0 )
    num_correct = np.sum( true_labels == pred_labels )

    print 'ran for %d iterations' % num_iter
    print 'inputs:'
    print inputs
    print 'targets:'
    print targets
    print 'predictions:'
    print predictions
    print 'sum sq. err:', sse
    print 'accuracy:', float(num_correct) / len(true_labels)
