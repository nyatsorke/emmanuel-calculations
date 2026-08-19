Count=0
Sum=0
Num=float(input("Enter first Number: "))
Count=Count + 1
Sum=Sum+Num
while Count < 4 :
    Num=float(input("Enter next Number: "))
    Count=Count + 1
    Sum=Sum+Num
Average=Sum/Count
print("the average is:",Average)