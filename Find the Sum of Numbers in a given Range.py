num1 = list(map(int, input("Enter multiple values: ").split()))
sum = 0
for i in range(num1[0], num1[1]+1):
    sum += i
print(sum)
