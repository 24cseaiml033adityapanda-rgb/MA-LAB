lowerlimit = []
upperlimit = []
frequency = []
mid_value = []
mean = []
c_freq=[]


n = int(input("Enter the number of classses : "))
for i in range(n):
    a = int(input(f"Enter lower limit {i+1}: "))
    lowerlimit.append(a)
    b = int(input(f"Enter upper limit {i+1}: "))
    upperlimit.append(b)
    c = int(input("Enter frequency : "))
    frequency.append(c)
    mid_value.append((a+b)/2)

for i in range(n):
    mean.append(frequency[i]*mid_value[i])
print("Mean : ",sum(mean)/sum(frequency))

sum1=0

for i in range(n):
    sum1+=frequency[i]
    c_freq.append(sum1)

for i in range(n):
    if(c_freq[i]>=(sum1/2)):
        median_class=i
        break

l=lowerlimit[median_class]
f=frequency[median_class]
cf=0 if median_class==0 else c_freq[median_class-1]

h=upperlimit[median_class]-lowerlimit[median_class]

median = l+(h*(((sum1/2)-cf)/f))

print("Median : ",median)

modal_class = frequency.index(max(frequency))
l=lowerlimit[modal_class]
f1=frequency[modal_class]
f0=0 if modal_class==0 else frequency[modal_class-1]
f2=0 if modal_class==n-1 else frequency[modal_class+1]
h=upperlimit[modal_class]-lowerlimit[modal_class]
mode = l + ((f1 - f0) / ((2 * f1) - f0 - f2)) * h
print("Mode : ",mode)