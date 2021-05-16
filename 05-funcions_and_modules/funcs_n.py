# funcs 1
import random
data=[]
for x in range(100):
	if random.randint(1,100)<33:
		data.append(x)

def find(a,b,key):
	i=round((a+b)/2)
	if 0 <= i < len(data) and i != a and i != b:
		if data[i]==key:
			return i
		if data[i]>key:
			return find(a,i,key)
		else:
			return find(i,b,key)
	return -1
print(find(0,len(data)-1,50))

