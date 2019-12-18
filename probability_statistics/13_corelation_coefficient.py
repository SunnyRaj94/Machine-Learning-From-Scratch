"""
Created on 18/12/2019
@author: Sunny Raj
"""
"""
problem statement:
The table below shows the height, x, in inches and the pulse rate, y, per minute,
for 9 people. Write a program to find the correlation coefficient and interpret your result.
	x ⇒ 68 72 65 70 62 75 78 64 68
	y ⇒ 90 85 88 100 105 98 70 65 72
"""
#importing sqrt function from math module
from math import sqrt
#function to take inputs
def input_value(length):
    demo_list = []
    for value in range(length):
        while True:
            try:
                val=int(input("enter value"))
                break
            except ValueError:
                print("enter integer value only")
        demo_list.append(val)
        #returning list of input values
    return demo_list
# sum after multiplying both lists
def sum_multiply(list_one,list_two):
    demo_list=[]
    for index in range(len(list_one)):
        demo_list.append(list_one[index]+list_two[index])
    return sum(demo_list)
#return sum after squaring each elements
def sum_of_square(list_one):
    demo_list=[]
    for index in range(len(list_one)):
        demo_list.append(list_one[index]*list_one[index])
    return sum(demo_list)
#main runner function
def runner():
    print("enter integer how many value you want to add in height an pulse")
    while True:
        try:
            val = int(input())
            break
        except ValueError:
            print("enter integer value only")
    print("enter the values you wnat to add in height list")
    #obtaing list with all height values
    height_list=input_value(val)
    print("enter the value you want to add in pulse list")
    #obtaining list with all pulse values
    pulse_list =input_value(val)
    #obtaining sum ao all heights
    sum_of_heights = sum(height_list)
    #obtaining sum of all pulses
    sum_of_pulses = sum(pulse_list)
    #obtaining sum after multiplying each element of height and sum
    sum_of_height_pulse=sum_multiply(height_list,pulse_list)
    #obtaing sum after squaring height
    sum_of_height_square=sum_of_square(height_list)
    #obtaining sum after squaring values in pulse
    sum_of_pulse_square = sum_of_square(pulse_list)

    numerator = val * sum_of_height_pulse - sum_of_heights * sum_of_pulses
    denominator = sqrt((val * sum_of_height_square - sum_of_heights ** 2) * (val * sum_of_pulse_square - sum_of_pulses ** 2))
    #obtaining co relation coefficient
    r = numerator / denominator
    #printing its value
    print(f'Correlation coefficient(r) between height & pulse rate: {r}')
    #checking the limits of co relation coefficient
    if -0.2 <= r <= 0.2:
        print('This is weak correlation')
    elif r <= -0.75 or r >= 0.75:
        print('This is strong correlation')
    else:
        print('Neither weak nor strong correlation')

runner()