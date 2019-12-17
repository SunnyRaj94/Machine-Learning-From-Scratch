"""
Created on 16/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a python program to add two matrices
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
#method to return matrix after adding two matrices
def add_matrices(matrix_one,matrix_two,row,col):
    #initializing empty matrix
    matrix = []
    #looping through the row value
    for index_x in range(row):
        #initializing a temp variable
        temp = []
        #looping through the column value
        for index_y in range(col):
            #adding both values
            value = matrix_one[index_x][index_y]+matrix_two[index_x][index_y]
            temp.append(value)
        matrix.append(temp)
    return matrix
#function to print row wise matrix
def display_matrix(matrix):
    for mat in matrix:
        print(mat)

#main or driver function
try:
    def runner():
        while True:
            try:
                print("enter row value for first matrix")
                #taking value of row for matrix one
                row_one = criteria_setup()
                print("enter column value for first_matrix ")
                # taking value of column for matrix one
                col_one = criteria_setup()
                print("enter row value for second matrix")
                # taking value of row for matrix two
                row_two = criteria_setup()
                print("enter column value for second matrix ")
                # taking value of column for matrix two
                col_two = criteria_setup()
                assert row_one==row_two and col_two== col_one
                break
            except AssertionError:
                print("try again")
        print("enter values for first matrix")
        matrix_one = value_input(row_one, col_one)
        print("enter value for second matrix")
        matrix_two = value_input(row_two, col_two)
        print("first matrix")
        display_matrix(matrix_one)
        print("second matrix")
        display_matrix(matrix_two)
        added_matrix = add_matrices(matrix_one, matrix_two, row_one, col_one)
        print("matrix after addition")
        display_matrix(added_matrix)
except Exception:
    print("re run the program")


runner()