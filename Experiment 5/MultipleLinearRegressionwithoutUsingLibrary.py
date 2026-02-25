def transpose(A):
    """Returns the teanspose of a 2D list."""
    return [[A[j][i] for j in range (len(A))] for i in range(len (A[0]))]

def multiply(A,B):
    """Multiply two matrix or a mantrix and a vector."""
    # Check if B is a 1D vector
    is_b_1d = isinstance(B[0],(int,float))
    if is_b_1d:
        return [sum(A[i][k]*B[k] for k in range(len(B))) for i in range](len(A))
    else:
        #Standrad matrix multiplication
        result=[[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k]*B[k][j]
    return result

def invert_matrix(matrix):
    """Inverse a square matrix using Gauss-Jordan elimination"""
    n=len(matrix)
    #create a identity matrix
    identity = [[float(i==j) for j in range(n)]for i in range(n)]
    #Work on a copy to avoid modifying the original 
    AM = [row[:] for row in matrix]

    for i in range(n):
        #Partial Pivoting
        max_el = abs(AM[i][i])
        max_row = i
        for k in range(i+1,n):
            if abs(AM[k][i]) > max_el:
                max_el = abs(AM[k][i])
                max_row = k
        if max_el < 1e-10:
            return None #Matrix is singular
        
        AM[i], AM[max_row] = AM[max_row],AM[i]
        identity[i],identity[max_row] = identity[max_row],identity[i]

        #Normalixe the pivot row
        pivot = AM[i][i]
        for j in range(i,n):
            AM[i][j] /= pivot
        for j in range(n):
            identity[i][j] /= pivot
        
        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = AM[k][i]
                for j in range(i,n):
                    AM[k][j] -= factor*AM[i][j]
                for j in range(n):
                    identity[k][j] -= factor*identity[i][j]
    return identity

# ---Main Program---

try:
    print("---Multiple Linear Regression---")
    #1. Get Dimention
    n=int(input("Enter number of data points (rows): "))
    k=int(input("Enter number of features (independent variables) : "))

    # 2. GET X DATA(FEATUES)
    print(f"\nEnter the {k} features for each row : ")
    X = []
    for i in range(n):
        while True:
            