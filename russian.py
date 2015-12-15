##: The Russian Peasant's Algorithm (Ancient Egyptian Multiplication)
##: Been around for a long long time. (Seventeenth Century B.C.)

##: Multiply two numbers together.
##: Requirements: multiply by 2, divide by 2, and Add numbers

##: AKA =  Mediation and Duplation Method

##:
##: Inputs ->  two numbers
##: Output ->  the solution to those two numbers
##:             multiplied together using the Russian Peasent Algorithm

# 17 in base 2:  10001 = 17           10001
#                 >> 1                 << 1
#                 1000 = 8           100010 = 34

import time

CACHE = {} #The cache stores the results from previous calls to russian

def russian(a,b):
    key = (a,b)
    if key in CACHE: #Have we already done this computation?
        z = CACHE[key]
    else: #If not, then run the russian peasant's algorithm...
        print 'Not in Cache'
        x = a; y = b                    ## Semicolon -> Compound Statement
        z = 0                           ## Acumulator
        while x > 0:                    ## While Loop Begins
            if x % 2 == 1: z = z + y    ## Modulo operator
            y = y << 1                  ## Shift Binary over to left
            x = x >> 1                  ## Shift Binary over to right
            
        #Finally, store the result in the cache
        CACHE[key] = z
    return z                        ## Return Z

def test_russian():
    start_time = time.time()
    print russian(357,16)
    print "Russian Algorithm took %f seconds" % (time.time()-start_time)

    start_time = time.time()
    print russian(357,16)
    print "Russian Algorithm took %f seconds" % (time.time()-start_time)

    assert russian(357,16) == 5712

test_russian()