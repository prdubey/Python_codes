# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:34:07 2022

@author: prdubey
"""
'''
class genPrimes(object):
    def __init__(self):
        self.initPrime = 1
    
    def findNextPrime(self):
        listOfPrimes = []
        next = self.initPrime
        while True:
            if 
'''
def genPrimes():
    listOfPrimes = []
    nextPrime = 2
    tag = 0
    while True:
        #print(nextPrime)
        cpPrimes = listOfPrimes[:]
        if listOfPrimes == []:
            listOfPrimes.append(2)
            next = nextPrime
            yield next #prints the value assigned to next
            nextPrime = next + 1
        else:
            for i in cpPrimes:
                if nextPrime % i == 0 :
                    tag = 1
                    break
                else:
                    tag = 0
            next = nextPrime
            if tag == 0:
                listOfPrimes.append(nextPrime)
                yield next
                nextPrime = next + 1
            else:
                nextPrime = next + 1
    return listOfPrimes
    
           
            



#print(genPrime())
primeGenerator = genPrimes()
#primeGenerator.__next__()

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

#print(genFib())
    
        
        
        