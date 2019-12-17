"""
Created on 16/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to perform multiplication of given matrix and vector
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

#function to print row wise matrix
def display_matrix(matrix):
    for mat in matrix:
        print(mat)

#function that will take matrix and scalar matrix as input and gives multiplication of that
def vector_multiplication(row_one,col_one,row_two,col_two,matrix_one,matrix_two):
    #initializing an empty matrix to save result
    matrix = []
    #looping through the row of first matrix
    for col in range(row_one):
        temp = []
        #looping through the column of second matrix
        for row in range(col_two):
            temp.append(0)
        matrix.append(temp)
    #doing the multiplication
    for index_x in range(len(matrix_one)):
        for index_y in range(len(matrix_two[0])):
            for index_z in range(len(matrix_two)):
               matrix[index_x][index_y] += matrix_one[index_x][index_z] * matrix_two[index_z][index_y]
    #returning the multiplied matrix
    return matrix

#runner function which is letting ecexuting this module
def runner():
    while True:
        try:
            print("Enter row value for first matrix")
            row_one=criteria_setup()
            print("Enter column value for first matrix")
            col_one = criteria_setup()
            print("enter row value for second matrix")
            row_two = criteria_setup()
            print("enter column value for second matrix")
            col_two=criteria_setup()
            assert (row_two==1 or col_two==1) and (col_two==row_one or col_one==row_two)
            break
        except AssertionError:
            print("value of row of second matrix must be one and "
                  "value of rows of first matrix must be equal to columns of second matrix")
    print("Start entering value for matrix one")
    matrix_one= value_input(row_one,col_one)
    print("start entering values for matrix two")
    matrix_two=value_input(row_two,col_two)
    print("your entered first matrix is :")
    display_matrix(matrix_one)
    print("your entered second matrix ix :")
    display_matrix(matrix_two)
    multiplied_matrix=vector_multiplication(row_one,col_one,row_two,col_two,matrix_one,matrix_two)
    print("matrix after multiplication is :")
    display_matrix(multiplied_matrix)

runner()