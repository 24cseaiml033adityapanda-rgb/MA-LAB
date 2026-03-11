def transpose(A):
    """Returns the teanspose of a 2D list."""
    return [[A[j][i] for j in range (len(A))] for i in range(len (A[0]))]

def multiply(A,B):
    """Multiply two matrix or a mantrix and a vector."""
    # Check if B is a 1D vector
    is_b_1d = isinstance(B[0],(int,float))
    if is_b_1d:
        return [sum(A[i][k] * B[k] for k in range(len(B))) for i in range(len(A))]
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
            try:
                row_input = input(f"Row {i+1} features : ").split()
                row = [float(val) for val in row_input]
                if len(row) != k:
                    print(f"Error: Expected {k} values. Please try again")
                    continue
                #Add 1.0 at index 0 for the Intercept(B0)
                X.append([1.0]+row)
                break
            except ValueError:
                print("Error: Invalid input. Enter numbers only")
    
    #3. GET Y DATA (TARGET)
    print(f"\nEnter the {n} target values (Y) separated by spaces: ")
    while True:
        try:
            y_input=input("Y values: ").split()
            if len(y_input) != n:
                print(f"Error: Expected {n} values. Please try again.")
                continue
            Y = [float(val) for val in y_input]
            break
        except ValueError:
            print("Error: Invalid input. Enter numbers only.")

    #4. Math: Normal Equationn(Beta = (X'X)^-1 X'Y)
    XT = transpose(X)
    XTX = multiply(XT,X)
    XTX_inv = invert_matrix(XTX)
    
    if XTX_inv is None:
        print("\n[!] Error: The matrix is singular (non-invertible). Check for reductunt data")
    else:
        XTY = multiply(XT,Y)
        beta = multiply(XTX_inv,XTY)

        #5.OUTPUT RESULTS
        print("\n"+"="*45)
        print(f"{'variable':<20} | {'Coefficient':<15}")
        print("-"*45)
        print(f"{'Intercept (B0)':<20} | {beta[0]:.4f}")
        for i in range(1,len(beta)):
            print(f"{f'Feature X{i} (B{i})':<20} | {beta[i]:.4f}")
        print("="*45)
except Exception as e:
    print(f"\nAn error occoured: {e}")

    """
    Output:
    ---Multiple Linear Regression---
Enter number of data points (rows): 5
Enter number of features (independent variables) : 2

Enter the 2 features for each row :
Row 1 features : 12 2
Row 2 features : 13 4
Row 3 features : 14 5
Row 4 features : 15 7
Row 5 features : 16 8

Enter the 5 target values (Y) separated by spaces:
Y values: 134 156 234 234 123

=============================================
variable             | Coefficient
---------------------------------------------
Intercept (B0)       | 1087.9333
Feature X1 (B1)      | -88.4000
Feature X2 (B2)      | 62.6667
=============================================
    """