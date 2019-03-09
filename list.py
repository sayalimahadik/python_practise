
def odd_add():
	x=[1,2,3,4,5,6,7,8,9,10]
	c=len(x)
	t=0
	for i in range(0,c):
		if x[i]%2==0:
			continue
		else:
			t=t+x[i]
			print(t)

odd_add()