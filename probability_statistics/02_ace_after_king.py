"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to find the probability of drawing an ace after drawing a king on the first draw
"""
#we know pack of cards have 52 cards
pack=52
#number of ace in pack are 4
number_of_aces=4
#number of king in pack are 4
number_of_kings=4
#probaility of finding a king first
prob_king = 4/52
#now 51 cards are left
#so probability to find ace out of those are 4/51
prob_ace=4/51
total_probability = prob_king*prob_ace
print("probability of drawing an ace after drawing a king on the first draw is : ",total_probability)