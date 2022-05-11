#without usin max funtion
num =  list(map(int, input("enter number : ").split()))
print(f"this is greatest : {num[0]}") if num[0] > num[1] else print(f"this is greatest : {num[1]}")
