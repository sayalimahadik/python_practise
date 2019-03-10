print("Enter the number: ")
a=int(input())

def prime_no():
	# for x in range(1,(a+1)):
	# 	if a%x==0:
	# 		print(f"{x}")
	# 		if x%2==0:
	# 			print(f"{x} notprime no.")
	# 	else:			
	# 		print(f"{x}prime no.")


	for i in range(2,a):
		if a%i==0:
			print(f"{a} not prime number")
			break
		else:
			print(f"{a} prime number")
			# continue
prime_no()