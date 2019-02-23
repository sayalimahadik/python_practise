x=[1,2,3,4,5,6,7,8,9,10]
# z=[i**3 for i in x]
# print(z)
# print("\n\n")

# y=[]
# z=[]
# for i in x:
# 	if i%2==0:
# 		y.append(i)
# 		print(y)

# 	else:
# 		z.append(i)
# 		print(z)

t=[i/2 if i%2==0 else i**2 for i in x]
print(t)


c=[i*"*" for i in x]
print(c)

