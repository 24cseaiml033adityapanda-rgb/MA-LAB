def transpose(A):
  return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def multiply(A, B):
  is_b_1d = isinstance(B[0], (int, float))
  if is_b_1d:
    return [sum(A[i][k] * B[k] for k in range(len(B))) for i in range(len(A))]
  else:
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
      for j in range(len(B[0])):
        for k in range(len(B)):
          result[i][j] += A[i][k] * B[k][j]
    return result

def invert_matrix(matrix):
  n = len(matrix)
  identity = [[float(i == j) for j in range(n)] for i in range(n)]
  AM = [row[:] for row in matrix]
  for i in range(n):
    max_el = abs(AM[i][i])
    max_row = i
    for k in range(i + 1, n):
      if abs(AM[k][i]) > max_el:
        max_el = abs(AM[k][i])
        max_row = k

    if max_el < 1e-10:
      return None

    AM[i], AM[max_row] = AM[max_row], AM[i]
    identity[i], identity[max_row] = identity[max_row], identity[i]

    pivot = AM[i][i]
    for j in range(i, n):
      AM[i][j] /= pivot
    for j in range(n):
      identity[i][j] /= pivot

    for k in range(n):
      if k != i:
        factor = AM[k][i]
        for j in range(i,n):
          AM[k][j] -= factor * AM[i][j]
        for j in range(n):
          identity[k][j] -= factor * identity[i][j]

  return identity

try:
  print("--- Multivariate Regression (Manual Calculation) ---")

  n = int(input("Enter the number of data points (rows): "))
  k = int(input("Enter the number of features (independent variables): "))
  m = int(input("Enter the number of targets (dependent variables): "))

  # 1. GET X DATA (Features)
  print(f"\nEnter the {k} features for each row:")
  X = []

  for i in range(n):
    while True:
      try:
        row_input = input(f"Row {i+1} features: ").split()
        row = [float(val) for val in row_input]

        if len(row) != k:
          print(f"Error: Expected {k} values. Please try again.")
          continue

        X.append([1.0] + row)   # Add intercept
        break

      except ValueError:
        print("Invalid input. Enter numeric values only.")

  # 2. GET Y DATA (Multiple Targets)
  print(f"\nEnter the {m} target values for each row:")

  Y = []

  for i in range(n):
    while True:
      try:
        row_input = input(f"Row {i+1} targets: ").split()
        row = [float(val) for val in row_input]

        if len(row) != m:
          print(f"Error: Expected {m} values. Please try again.")
          continue

        Y.append(row)
        break

      except ValueError:
        print("Invalid input. Enter numeric values only.")

  # 3. CALCULATIONS
  XT = transpose(X)
  XTX = multiply(XT, X)
  XTX_inv = invert_matrix(XTX)

  if XTX_inv is None:
    print("\n[!] Error: Matrix is singular (non-invertible). Check data.")

  else:
    XTY = multiply(XT, Y)
    BETA = multiply(XTX_inv, XTY)

    # 4. PRINT RESULT
    print("\n" + "="*60)
    print("Regression Coefficients Matrix")
    print("="*60)

    for i in range(len(BETA)):
      if i == 0:
        var = "Intercept (b0)"
      else:
        var = f"Feature X{i}"

      print(f"{var:<15} :", end=" ")

      for j in range(len(BETA[0])):
        print(f"B{i}{j+1} = {BETA[i][j]:.4f}", end="   ")

      print()

    print("="*60)

except Exception as e:
  print(f"An error occurred: {e}")

     
"""
Output:
Multivariate Regression (Manual Calculation) 
Enter the number of data points (rows): 5
Enter the number of features (independent variables): 1
Enter the number of targets (dependent variables): 2

Enter the 1 features for each row:
Row 1 features: 1 -1
Error: Expected 1 values. Please try again.
Row 1 features: 0
Row 2 features: 1
Row 3 features: 2
Row 4 features: 3
Row 5 features: 4

Enter the 2 target values for each row:
Row 1 targets: 1 -1
Row 2 targets: 4 -1
Row 3 targets: 3 2
Row 4 targets: 8 3
Row 5 targets: 9 2

============================================================
Regression Coefficients Matrix
============================================================
Intercept (b0)  : B01 = 1.0000   B02 = -1.0000   
Feature X1      : B11 = 2.0000   B12 = 1.0000   
============================================================
"""