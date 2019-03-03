print("enter the input: ")
a= input()
# print("enter the input which is how many times are repeated:  ")
# b=input()
# z=a.count(b)
# print(f"{b} is {z} time repeated")
# print("enter the input which is how many times are repeated:  ")
# c=input()
# x=a.count(c)
# print(f"{c} is {x} time repeated")
# c=len(a)
# print(c)

v=[]
s=[]
# j=a.split(",")
# print(j)

c=len(a)
print(c)


for x in range(0,(c)):
	# print(x)
	v.append(a[x])
# print(v)
z=len(v)
print(z)
for y in range(0,(z)):
	s.append(v.count(v[y]))
# print(s)
	# if s>1:
	# 	print(only one letter)
	# else:
	# 	print(not)

print(f"{v} is {s} time repeat")



