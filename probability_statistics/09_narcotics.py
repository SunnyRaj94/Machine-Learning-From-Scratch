"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. 
Overall, five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances). 
Out of all the people prescribed pain pills, 8% are addicts. 
If a patient is an addict, write a program to find the probability that they will be prescribed pain pills?
"""
#importing fractions module
from fractions import Fraction
#0% of patients are prescribed narcotic pain killers
prescribed_pain_pills = Fraction(10,100)
#five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances)
addicted_patients=Fraction(5,100)
#Out of all the people prescribed pain pills, 8% are addicts.
addicted_and_prescribed = Fraction(8,100)
#probability that they will be prescribed pain pills
probability_prescribed_and_addicted =(addicted_and_prescribed*prescribed_pain_pills)/addicted_patients
#printing the output
print("probability that an addicted patient is prescribed to pain pills is : ",round(probability_prescribed_and_addicted,4)*100," %")