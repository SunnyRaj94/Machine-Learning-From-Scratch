"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
You toss a fair coin three times write a program to find following:
What is the probability of three heads, HHH?
What is the probability that you observe exactly one heads?
Given that you have observed at least one heads, what is the probability that you observe at least two heads?
"""
#list out the possibilities A= HTT, THT, THH, HHT, THH, HTH,HHH
#so total 8 possibilities
prob_three_heads=1#only one time it can occur
print("probability of three heads is : ",prob_three_heads/8)
prob_exact_one_head = 2#only two times it occured
print("probability of exactly one head : ",prob_exact_one_head/8)
prob_atleast_two_head = 5
print("probability atleast two heads : ",prob_atleast_two_head/8)