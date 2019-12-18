"""
Created on 18/12/2019
@author: Sunny Raj
"""
"""
problem statement:
X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4.
    Write a program to find 
    a. P(x < 40) 
    b. P(x > 21) 
    c. P(30 < x < 35)
"""
#given mean =30
mean =30
#given standard deviation
standard_deviation = 4
#we have to find fo value 40 given
value_one=40
#given value two
value_two = 21
#given values
value_three_start = 30
value_three_stop = 35
#calculating z score for value
z_score_one = (value_one-mean)/standard_deviation
#calculating z score for value
z_score_two = (value_two-mean)/standard_deviation
#calculating z score for value
z_score_three_start = (value_three_start-mean)/standard_deviation
#calculating z score for value
z_score_three_stop = (value_three_stop-mean)/standard_deviation
#printing the output
print("zcore for 40 is : ",z_score_one," P(x < 40 ) is : ",0.9938)
print("zcore for 21 is : ",z_score_two," P(x > 21 ) is : ",1-0.0122)
print("zcore for 30 is : ",z_score_three_start," P(x < 30 ) is : ",0)
print("zcore for 35 is : ",z_score_three_stop," P(x > 35 ) is : ",0.8944)