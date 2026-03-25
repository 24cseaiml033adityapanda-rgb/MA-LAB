n = int(input("Enter number of data points: "))
p = int(input("Enter the number of independent variables: "))

X = [[0]*p for _ in range(n)]
y = []

for i in range(n):
    for j in range(p):
        X[i][j] = input(f"Enter the {j+1} independent variable (string) for row {i+1}: ")
    y.append(input(f"Enter target class for row {i+1}: "))

target_classes = list(set(y))

input_point = []
for j in range(p):
    input_point.append(input(f"Enter input value (string) for variable {j+1}: "))

stats = {cls: {'count': 0, 'feature_counts': [{} for _ in range(p)]} for cls in target_classes}

for idx, cls in enumerate(y):
    stats[cls]['count'] += 1
    for j in range(p):
        val = X[idx][j]
        if val not in stats[cls]['feature_counts'][j]:
            stats[cls]['feature_counts'][j][val] = 0
        stats[cls]['feature_counts'][j][val] += 1

posteriors = {}
total_count = n

for cls in target_classes:
    prior = stats[cls]['count'] / total_count
    likelihood = 1
    for j in range(p):
        val = input_point[j]
        count = stats[cls]['feature_counts'][j].get(val, 0) + 1
        total = stats[cls]['count'] + len(stats[cls]['feature_counts'][j])
        likelihood *= count / total
    posteriors[cls] = prior * likelihood

predicted_class = max(posteriors, key=posteriors.get)
print("Predicted target class is:", predicted_class)
