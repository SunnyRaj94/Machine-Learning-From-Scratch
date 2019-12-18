"""
Created on 18/12/2019
@author: Sunny Raj
"""
"""
problem statement:
A radar unit is used to measure speeds of cars on a motorway. 
The speeds are normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. 
Write a program to find the probability that a car picked at random is travelling at more than 100 km/hr? 
"""
#given mean =90
mean =90
#given standard deviation
standard_deviation = 10
#we have to find fo value 40 given
value_one=100
#calculating z score for value
z_score_one = (value_one-mean)/standard_deviation
#printing the output
print("zcore for 100 is : ",z_score_one," P(speed < 100 ) is : ",1- 0.8413)