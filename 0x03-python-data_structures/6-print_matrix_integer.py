#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each element in the current row
        for j in range(len(matrix[i])):
            # Check if the element is not the last element in the row
            if j < len(matrix[i]) - 1:
                # Print the element with a space after it
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                # Print the last element without a space after it
                print("{:d}".format(matrix[i][j]), end="")
        # Print a new line after each row
        print("")
