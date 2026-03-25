n = int(input("Enter number of data points: "))
k = int(input("Enter the K value: "))
p = int(input("Enter the number of independent variables: "))

X = [[0]*p for _ in range(n)]
y = []

for i in range(n):
    for j in range(p):
        X[i][j] = float(input(f"Enter the {j+1} independent variable for row {i+1}: "))
    y.append(input(f"Enter target class for row {i+1}: "))

target_classes = []
for val in y:
    if val not in target_classes:
        target_classes.append(val)

input_point = []
for j in range(p):
    input_point.append(float(input(f"Enter input value for variable {j+1}: ")))

d = []
for i in range(n):
    sum_sq = 0
    for j in range(p):
        sum_sq += (X[i][j] - input_point[j])**2
    d.append((sum_sq**0.5, y[i]))

d.sort(key=lambda x: x[0])

target_freq = {cls: 0 for cls in target_classes}
for i in range(k):
    target_freq[d[i][1]] += 1

predicted_class = max(target_freq, key=target_freq.get)

print("Target output is:", predicted_class)