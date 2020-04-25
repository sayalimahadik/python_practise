print("******NEW CALCULATOR*******")
a=int(input("enter your first value: \n"))
b=int(input("enter your second value: \n"))
k=input("select your operation 1/2/3/4/5/6/7: \n")
x=a+b   
y=a-b
z=a*b
u=a/b
v=a//b
w=a%b
r=a**b
print("\n")
if k=="1":
	print(f"addition of the two number :  {a}+{b}= ",f"{x}\n\n")

elif k=="2":
	print(f" subtraction of two number : {a}-{b}= ",f"{y}\n\n")
elif k=="3":
	print(f" multification of two number : {a}*{b}= ",f"{z}\n\n")
elif k=="4":
	print(f" division of two number : {a}/{b}= ",f"{u}\n\n")
elif k=="5":
	print(f" floor division of  number : {a}//{b}= ",f"{v}\n\n")
elif k=="6":
	print(f" modulus of number : {a}%{b}= ",f"{w}\n\n")
elif k=="7":
	print(f" exponanation of number : {a}**{b}= ",f"{r}\n\n")
else:
	print("error")