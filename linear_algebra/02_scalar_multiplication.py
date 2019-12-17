"""
Created on 16/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to perform scalar multiplication of matrix and a number
"""
#method to setup the value of row and column for input matrices
def criteria_setup():
    while True:
        try:
            value=int(input())
            break
        except ValueError:
            print("try again with proper value")
    return value
# method/function to take input in matrix
def value_input(row,col):
    #initializing empty matrix
    matrix = []
    #looping through the given row value
    for index_x in range(row):
        #initializing a temperory variable
        temp=[]
        #looping through the given column value
        for index_y in range(col):
            while True:
                try:
                    value = int(input("enter value for [{}],[{}]".format(index_x,index_y)))
                    break
                except ValueError:
                    print("try again with proper integer value")
            #adding values to one row
            temp.append(value)
        #Aadding list into a list
        matrix.append(temp)
        #returning the 2d list / matrix
    return matrix

#method to return matrix after scalar addition
def add_scalar(matrix_one,add_value,row,col):
    #initializing empty matrix
    matrix = []
    #looping through the row value
    for index_x in range(row):
        #initializing a temp variable
        temp = []
        #looping through the column value
        for index_y in range(col):
            #adding both values
            value = matrix_one[index_x][index_y]+add_value
            temp.append(value)
        matrix.append(temp)
    return matrix
#function to print row wise matrix
def display_matrix(matrix):
    for mat in matrix:
        print(mat)


def runner():
    print("enter row value for matrix")
    #taking value of row for matrix
    row= criteria_setup()
    print("enter column value for matrix ")
    # taking value of column for matrix
    col= criteria_setup()
    print("enter value that needs to do scalar addition with")
    # taking value that needs to do scalar addition with
    add_value= criteria_setup()
    print("enter values for matrix")
    matrix= value_input(row, col)
    print("matrix before addition")
    display_matrix(matrix)
    added_matrix = add_scalar(matrix,add_value,row,col)
    print("matrix after addition")
    display_matrix(added_matrix)

runner()