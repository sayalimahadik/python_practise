import random
r = random.randint(1,20)

print("Guess the number:")
x=int(input())

if x<r:
	print("Guessed number is less")
elif x==r:
	print("You guessed is right!!!!")
else:
	print("Guessed number is large")