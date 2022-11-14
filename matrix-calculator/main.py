# MATRIX CALCULATOR USING NUMPY
import numpy as np


def ask(m, n):  # method to get matrix input from user
    print('Enter each element row wise :')
    matrix = []
    for r in range(m):
        temp = []
        for c in range(n):
            temp.append(float(input(" ")))
        matrix.append(temp)
    return np.array(matrix)


res = None  # last result
while True:  # main loop
    print("""
==============================================================================================
Welcome to simple matrix calculator
1: Matrix summation (Row and column must be the same)
2: Matrix subtraction (row and column must be the same)
3: Matrix multiplication (A column and B row must be the same)
4: Matrix multiplication(constant number)
5: Transpose
6: Determinant (Matrix must be square)
7: Inverse (Matrix must be square)
c: clear last result
-1: Exit
# The last result will be set as the Matrix A value, enter c if you want a new Matrix A value
                """)
    print(f'Last result : \n{res}\n')
    try:
        user_input = input('Your choice : ').lower()

        if user_input == '-1':  # exit the loop
            break
        elif user_input == 'c':  # clear last result
            res = None
            print('Last result cleared')

        # MATRIX SUMMATION
        elif user_input == '1':
            # check if there is no last result
            if res is None:
                row = int(input('Row : '))
                column = int(input('Column : '))
                A = ask(row, column)
                B = ask(row, column)
            else:
                A = res  # if there is a last result, the Matrix A value will be the last result
                B = ask(len(A), len(A[0]))
            res = A + B
            print(f'Matrix A \n{A}\n\nMatrix B\n{B}\n\nA + B \n{res}\n')

        # MATRIX SUBTRACTION
        elif user_input == '2':
            if res is None:
                row = int(input('Row : '))
                column = int(input('Column : '))
                A = ask(row, column)
                B = ask(row, column)
            else:
                A = res
                B = ask(len(A), len(A[0]))
            res = A - B
            print(f'Matrix A \n{A}\n\nMatrix B\n{B}\n\nA - B \n{res}\n')

        # MATRIX MULTIPLICATION
        elif user_input == '3':
            # check if there is no last result
            if res is None:
                m = int(input('Matrix A column : '))
                A = ask(int(input('Matrix A row : ')), m)  # i x m
                B = ask(m, int(input('Matrix B column : ')))  # m x n
            else:
                A = res  # if there is a last result, Matrix A value will be the last result
                B = ask(len(A[0]), int(input('Matrix B column : ')))
            res = np.matmul(A, B)
            print(f'Matrix A \n{A}\n\nMatrix B\n{B}\n\nA x B\n{res}\n')

        # MATRIX MULTIPLICATION TO A CONSTANT NUMBER
        elif user_input == '4':
            # check if there is no last result
            if res is None:
                mat = ask(int(input('Matrix row : ')), int(input('Matrix column : ')))
            else:
                mat = res  # if there is a last result, the last result will be set as the matrix
            num = float(input('Enter a contant number : '))
            res = mat * num
            print(f'Matrix \n{mat}\n\nMatrix x {num}\n\n{res}')

        # TRANSPOSE
        elif user_input == '5':
            if res is None:
                mat = ask(int(input('Matrix row : ')), int(input('Matrix column : ')))
            else:
                mat = res
            res = mat.transpose()
            print(f'Transposed \n{res}')

        # FIND DETERMINANT
        elif user_input == '6':
            if res is None:
                row_col = int(input('Matrix row and column : '))
                mat = ask(row_col, row_col)
            else:
                mat = res
            if len(mat) == len(mat[0]):
                print(f'Determinant : {round(np.linalg.det(mat))}')
            else:
                print('Matrix must be square')

        # INVERSE MATRIX
        elif user_input == '7':
            if res is None:
                row_col = int(input('Matrix row and column : '))
                mat = ask(row_col, row_col)
            else:
                mat = res
            if len(mat) == len(mat[0]):
                res = np.linalg.inv(mat)
                print(f'Determinant : \n{res}')
            else:
                print('Matrix must be square')

        else:
            print('Invalid Input')
    except ValueError as e:
        print('Invalid Input\n')
