"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
A bank teller serves customers standing in the queue one by one. 
Suppose that the service time XiXi for customer ii has mean EXi=2 (minutes) and Var(Xi)=1. 
We assume that service times for different bank customers are independent. 
Let YY be the total time the bank teller spends serving 50 customers. Write a program to find P(90<Y<110)
"""
#importing squareroot function to find square rooot
from math import sqrt
#given mean for each person
mean_for_each_person=2
#given variance of each person
variance_each_person=1
#since there are 50 persons
total_mean = mean_for_each_person*50
#since there are 50 persons
total_var=variance_each_person*50
#we know standard deviation equals to square root of variance
total_std_deviation= sqrt(total_var)
# calculating z-score for given data points
z_score = lambda x: (x - total_mean)/total_std_deviation
z_score_90 =z_score(90)
#checking through z table
z_value_90=0.0793
z_value_110=0.9207
z_score_110 =z_score(110)
#printing the values
print("z score for 90 minutes is : ",z_score_90)
print("P(Y < 90) : ",z_value_90)
print("z score for 110 minutes is : ",z_score_110)
print("P(Y < 110) : ",z_value_110)
#finding probability between both z score
print("probabability (90 < Y < 110) : ",z_value_110-z_value_90)
