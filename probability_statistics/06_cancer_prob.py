"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Given the following statistics, write a program to find the probability that a woman has cancer if she has a positive mammogram result?
		a. One percent of women over 50 have breast cancer.
		b. Ninety percent of women who have breast cancer test positive on mammograms.
		c. Eight percent of women will have false positives.
"""
#probability of having breast cancer
prob_breast_cancer=0.01
#probability of positive mammograms
prob_positive_mammogramms=0.9
#probability of false positive
prob_false_positive=0.08
# finding probability of all +ve tests i.e irrespective of cancer or not
total_positive = prob_breast_cancer*prob_positive_mammogramms + (1-prob_breast_cancer)*prob_false_positive
#finding the probablity that women has breasr cancer for positive mammograms
print("probability of having breast cancer with positive mammograms : ",prob_breast_cancer*prob_positive_mammogramms/total_positive)
