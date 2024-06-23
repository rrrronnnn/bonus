def input_matrix(matrix_name):
    """
    Function to input a matrix from user in the format specified in the problem.
    """
    matrix_str = input(f"Enter matrix {matrix_name}: ")
    rows = matrix_str.split('|')
    matrix = {}
    for i, row in enumerate(rows):
        elements = list(map(int, row.split(',')))
        matrix[i] = {j: elements[j] for j in range(len(elements))}
    return matrix

def multiply_matrices(U, V):
    """
    Function to multiply two matrices U and V.
    """
    n = len(U)
    M = {i: {j: 0 for j in range(n)} for i in range(n)}
    for i in range(n):
        for j in range(n):
            M[i][j] = sum(U[i][k] * V[k][j] for k in range(n))
    return M

def print_matrix(matrix):
    """
    Function to print a matrix in the required format.
    """
    for i in sorted(matrix.keys()):
        print([matrix[i][j] for j in sorted(matrix[i].keys())])

def main():
    """
    Main function to execute the matrix multiplication program.
    """
    U = input_matrix('U')
    V = input_matrix('V')
    M = multiply_matrices(U, V)
    print("M = U x V")
    print_matrix(M)

if __name__ == "__main__":
    main()
