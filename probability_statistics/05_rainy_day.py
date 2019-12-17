"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy traffic with probability 12, 
and given that it is not rainy, there will be heavy traffic with probability 14. If it's rainy and there is heavy traffic, 
I arrive late for work with probability 12. On the other hand, the probability of being late is reduced to 18 
if it is not rainy and there is no heavy traffic. In other situations (rainy and no traffic, not rainy and traffic) 
the probability of being late is 0.25. You pick a random day.
Write a program to find following
    What is the probability that it's not raining and there is heavy traffic and I am not late?
    What is the probability that I am late?
    Given that I arrived late at work, what is the probability that it rained that day?
"""

#Let R be the event that it's rainy,
# T be the event that there is heavy traffic,
# and L be the event that I am late for work
"""
The probability that it's not raining and there is heavy traffic
=2/3⋅1/4⋅3/4
=1/8.
"""
solution_one=1/8
"""
The probability that I am late .
=1/12+1/24+1/24+1/16
=11/48.
"""
prob_being_late =11/48
"""
the probability that it is raining when i am late is 
=1/12+1/24
=1/8.
"""
print("The probability that it's not raining and there is heavy traffic is :",solution_one)
print("The probability that I am late : ",11/48)
print("the probability that it is raining when i am late is : ",prob_being_late)