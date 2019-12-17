"""
Created on 16/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a program to find inverse matrix of matrix X
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

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    #initializing determinantt
    determinant = 0
    #looping in range length of matrix
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
#function to find transpose of matrix
def transposeMatrix(matrix):
    #returning transposed matrix
    return list(map(list,zip(*matrix)))
#function to find inverse of matrix
def getMatrixInverse(m):
    #determinant of given matrix
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    #finding co factors of each element wise
    for r in range(len(m)):
        #cofactors
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
def divide(matrix_one,div_value,row,col):
    #initializing empty matrix
    matrix = []
    #looping through the row value
    for index_x in range(row):
        #initializing a temp variable
        temp = []
        #looping through the column value
        for index_y in range(col):
            #adding both values
            value = matrix_one[index_x][index_y]/div_value
            temp.append(value)
        matrix.append(temp)
    return matrix


def runner():
    while True:
        try:
            print("Enter row value for first matrix")
            row = criteria_setup()
            print("Enter column value for first matrix")
            col = criteria_setup()
            assert row==col
            break
        except AssertionError:
            print("row and column value must be equal to find inverse of a matrix")
    print("your entered matrix is :")
    #obtaining matrix by input
    my_matrix = value_input(row,col)
    #displaying matrix
    display_matrix(my_matrix)
    #finding inverse by calling inverse function
    inverse_matrix=getMatrixInverse(my_matrix)
    #printing the inverse matrix
    print("inverse of given matrix is : ")
    display_matrix(inverse_matrix)

runner()