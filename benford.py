import random

for i in range(1,1000):
	#x = random.randrange(10,100)
	
	x = i
	
	y = int(str(x)[:1])
	
	z = str(y+1)+"0"
	
	r = int(z)/int(x)
	
	print(x, "---", str(r)[:5])
	
