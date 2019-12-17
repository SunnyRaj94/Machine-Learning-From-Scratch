"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to find the probability of drawing an ace after drawing an ace on the first draw
"""
#we know pack of cards have 52 cards
pack=52
#number of ace in pack are 4
number_of_aces=4
#probaility of finding a ace in  first draw
prob_ace_first = 4/52
#now 51 cards are left
#so probability to find ace out of those are 3/51
prob_ace=3/51
total_probability = prob_ace*prob_ace_first
print("probability of drawing an ace after drawing an ace on the first draw is : ",total_probability)