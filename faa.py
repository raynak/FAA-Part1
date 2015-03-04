import tp1 as tp1
import tp2 as tp2
import tp3 as tp3
import tp4 as tp4
import tp5 as tp5
import tp6 as tp6

import sys

# chaque tp a une fonction main

def usage():
    print "python2.7 faa.py [numero tp]"
    print "[numero tp] ={1..5}"
    return 0

if __name__ == '__main__':
    if (len(sys.argv)<2):
        usage()
    else:
        tp ={1 : tp1.main,
             #2 : tp2.main,
             #3 : tp3.main,
             #4 : tp4.main,
             5 : tp5.main,
             6 : tp6.main,
        }
        
        tp[int(sys.argv[1])]()
        
    
