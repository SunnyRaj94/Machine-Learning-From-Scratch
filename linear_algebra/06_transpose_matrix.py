"""
Created on 17/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to find transpose matrix 
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
def transposeMatrix(matrix):
    #returning transposed matrix
    return list(map(list,zip(*matrix)))

def runner():
    print("Enter row value for first matrix")
    row = criteria_setup()
    print("Enter column value for first matrix")
    col = criteria_setup()
    print("your entered matrix is :")
    # obtaining matrix by input
    my_matrix = value_input(row, col)
    # displaying matrix
    display_matrix(my_matrix)
    # finding transpose of matrix
    transpose_matrix = transposeMatrix(my_matrix)
    # printing the inverse matrix
    print("transpose of given matrix is : ")
    display_matrix(transpose_matrix)

runner()