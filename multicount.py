print("Enter the input: ")
a=input()
k=len(a)
# print(k)
for x in range(0,k):
	u=a[x]
	# print(u)
	r=a.count(a[x])
	print(f"{u} : {r}")


