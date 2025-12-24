unit=int(input("Enter the units  : "))
if unit<=100:
    bill=unit*1.5
    print(f"Your electricity bill is {bill}")
elif unit>100 and unit<=200:
    bill = (100*1.5) +(unit-100)*2.5
    print(f"Your electricity bill is {bill}")
else:
    bill=(100*1.5)+(100*2.5)+(unit-200)*4
    print(f"Your electricity bill is {bill}")

    
