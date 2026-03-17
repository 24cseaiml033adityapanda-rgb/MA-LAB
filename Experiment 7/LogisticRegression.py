import math

n = int(input("Enter number of samples: "))

X = []
y = []

print("Enter feature1, feature2, label (space separated) for each sample:")
for i in range(n):
    data = input().split()
    X.append([float(data[0]), float(data[1])])
    y.append(int(data[2]))

w1, w2 = 0.0, 0.0
b = 0.0

lr = 0.1
iterations = 1000

for it in range(iterations):
    dw1, dw2, db = 0.0, 0.0, 0.0
    for i in range(n):
        z = w1*X[i][0] + w2*X[i][1] + b
        y_pred = 1 / (1 + math.exp(-z)) # Sigmoid using math.exp
        error = y_pred - y[i]
        dw1 += error * X[i][0]
        dw2 += error * X[i][1]
        db += error

    dw1 /= n
    dw2 /= n
    db /= n

    w1 -= lr * dw1
    w2 -= lr * dw2
    b -= lr * db

print(f"\nLearned parameters:\nWeight1 = {w1}, Weight2 = {w2}, Bias = {b}")

print("\nEnter feature1 and feature2 for prediction:")
x1, x2 = map(float, input().split())
z = w1*x1 + w2*x2 + b
y_prob = 1 / (1 + math.exp(-z))
y_pred = 1 if y_prob >= 0.5 else 0
print("Predicted probability:", y_prob)
print("Predicted class:", y_pred)

'''
Output:
Enter number of samples: 5
Enter feature1, feature2, label (space separated) for each sample:
1 2 0
2 3 0
3 4 1
4 5 1
5 6 1

Learned parameters:
Weight1 = 3.4094016735126353, Weight2 = -1.0801601328473742, Bias = -4.489561806360004

Enter feature1 and feature2 for prediction:
3 5
Predicted probability: 0.5836663575174992
Predicted class: 1
'''