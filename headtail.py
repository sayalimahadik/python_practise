import random
r= random.randint(0,1)

print("\n\nPlayer 1st enter your side: \n\n")
x1=str(input())

print("\n\nPlayer 2nd enter your side: \n\n")
x2=str(input())

# head = 0
# tail = 1

if r == 0:
	print("\n\nCongrats....Coin Flipped to Heads...!!!!\n\n")
else:
	print("\n\nCongrats....Coin Flipped to Tails...!!!!\n\n")