"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
 In a communication system each data packet consists of 1000 bits. 
 Due to the noise, each bit may be received in error with probability 0.1. 
 It is assumed bit errors occur independently. 
 Find the probability that there are more than 120 errors in a certain data packet.
"""
from fractions import Fraction
from math import factorial
q = Fraction(1, 10)     # probability of failure i.e. error
p = 1 - q    # probability of success
n = 1000    # total trials

r = prob = 0    # total errors to be found
# we will calculate getting errors <= 120
while r <= 120:
    prob += factorial(n)*(p**(n-r))*(q**r)/(factorial(r)*factorial(n-r))
    r += 1

# getting probability that errors are more than 120 in a data packet
print(f'P (error(s) > 120): {round(float(1-prob), 4)*100} %')