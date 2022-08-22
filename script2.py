num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(num1,num2+1):
  if (Prime(i)):
    print(i,end=" ")
