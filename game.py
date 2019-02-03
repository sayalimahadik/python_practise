print("\n\n\n*****WELCOME TO GAME ROCK PAPER SCISSOR*****\n\n\n")

print("Enter the input of 1st player :")

x1=str(input())

# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("*** NO CHEATING\n\n"*40)

print("Enter the input of 2nd player :")

x2=str(input())

if x1:
	if x1== "rock":
		if x2=="paper":
			print("x2 is winner")

		elif x2=="scissor":
			print("x2 is winner")

		else:
			print("It's a draw..!!")

	if x1== "paper":
		if x2=="rock":
			print("x1 is winner")

		elif x2=="scissor":
			print("x2 is winner")

		else:
			print("It's a draw..!!")

	if x1== "scissor":
		if x2=="paper":
			print("x1 is winner")

		elif x2=="rock":
			print("x2 is winner")

		else:
			print("It's a draw..!!")

else:
	print("Enter the value please..!!")







# if x1== "rock" and x2=="paper":
# 	print("x2 is winner")

# elif x1=="rock" and x2=="scissor":
# 	print("x2 is winner")

# elif x1==x2:
# 	print("both are winner")

# if x1== "paper" and x2=="rock":
# 	print("x1 is winner")

# elif x1=="paper" and x2=="scissor":
# 	print("x2 is winner")

# elif x1==x2:
# 	print("both are winner")

# if x1== "scissor" and x2=="paper":
# 	print("x1 is winner")

# elif x1=="scissor" and x2=="rock":
# 	print("x2 is winner")

# elif x1==x2:
# 	print("both are winner")



