num=int(input("Enter a number:"))
if num<=0 or num>=0:
    if num<0:
        print(f"{num} is negative")
    elif num>0:
        print(f"{num} is positive")
    else:
        print(f"{num} is nutral")
