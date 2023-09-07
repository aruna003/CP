def matrix_multiply(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(M, n):
    print("n:",n)
    if n == 1:
        return M
    
    if n % 2 == 0:
        half_pow = matrix_power(M, n // 2)
        return matrix_multiply(half_pow, half_pow)
    
    else:
        half_pow = matrix_power(M, (n - 1) // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), M)

def fibonacciMatrixExponentiation(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Define the Fibonacci matrix
    F = [[1, 1], [1, 0]]

    # Use matrix exponentiation to calculate F^n
    result_matrix = matrix_power(F, n - 1)

    # The Fibonacci number is the top-left element of the result matrix
    return result_matrix[0][0]

n = 2  # Example: Calculate the 100th Fibonacci number
result = fibonacciMatrixExponentiation(n)
print(result)
