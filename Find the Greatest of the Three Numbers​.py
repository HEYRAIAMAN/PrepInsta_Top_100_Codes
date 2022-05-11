a,b,c =  list(map(int, input("enter number : ").split()))
print(f"this is greatest : {a}") if a > b and a > c else (print(f"this is greatest : {b}") if b > c else print(f"this is greatest : {c}"))
 