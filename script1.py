N = int(input("Enter the number: "))
# defining a function to check for prime
def Prime(num):
  if (num==1 or num==0):
    return False
  for i in range(2,num):
    if num % i == 0:
      return False
  return True


for n in range(1,N+1):
   if (Prime(n)):
     print(n,end=" ")



