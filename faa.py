import tp1 as tp1
import tp2 as tp2
import tp3 as tp3
import tp4 as tp4
import tp5 as tp5

import sys

# chaque tp à une fonction main

def usage():
    print "python2.7 faa.py [numero tp]"
    print "[numero tp] ={1..5}"
    return 0

if __name__ == '__main__':
    if (len(sys.argv)<2):
        usage()
    else:
        tp ={1 : tp1.main,
             2 : tp2.main,
             3 : tp3.main,
             4 : tp4.main,
             5 : tp5.main,
         }

        tp[sys.argv[1]]()
        
    
