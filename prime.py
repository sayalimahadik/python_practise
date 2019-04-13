print("enter your input: ")
a=int(input())
if a==2:
	print(f"{a} is prime number")


for i in range(2,a):

	if a%i==0:
		print(f"{a} not prime number")
		break
		
	
	if i>=(a-1):
		print(f"{a} prime number")