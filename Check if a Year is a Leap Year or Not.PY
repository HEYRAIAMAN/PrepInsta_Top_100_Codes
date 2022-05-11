year = int(input("enter the year : "))
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    print(f'this is leep year {year}')
else :
    print(f'this is not leep year {year}')
