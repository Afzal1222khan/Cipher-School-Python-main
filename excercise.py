# num1 = input("enter first number : ")
# num2 = input("enter first number : ")
# num3 = input("enter first number : ")
num1 , num2, num3 = input("enter three numbers comma separated").split(",")
print(f"average of three number :{(int(num1) + int(num2) + int(num3)) / 3}")
