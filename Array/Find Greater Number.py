a = [ 11,18,13,19,27]
max = a[0]

for i in range(len(a)):
    if a[1] > max:
        max = a[i]

print(max) 