n = int(input("Enter the number of data : "))
data = []
for i in range(n):
    value = float(input("Enter data : "))
    data.append(value)
mean = sum(data) / n
print("Mean :", mean)
data.sort()
if n % 2 == 0:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
else:
    median = data[n // 2]  
print("Median :", median)
data_count = {}
for item in data:
    if item in data_count:
        data_count[item] += 1
    else:
        data_count[item] = 1
max_count = max(data_count.values())
modes = [key for key, count in data_count.items() if count == max_count]
if len(modes) == n:
    print("No mode found") 
else:
    print("Mode :", modes)