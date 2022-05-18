import numpy as np
import matplotlib as mt
import matplotlib.pyplot as mtp 

#Basic_List
print("\t\tClass No 1\t\t")
a = [1,3,4] 				
b = [4,5,6]
c = b + a
print(f"The result is {c}")

mtp.plot(a,b)
mtp.show()

#DATA TYPE

#Int
e = 10	

#List
d = [5,6,7]               			
d.append(2)
print(f"List result{d}")

#tuple
t = (2,3,4)				  			

#Dictionary
f = {"name" : "arnob",				
	 "address" : "strt 10",
	 "phone" : 1976411722,
	}
f["height"] = 98			
print(f"Dictionary result",f["height"])

#nump array
g = np.array([1,2,4])
h = np.array([5,10,18])
print(f"Numpy array result",g)
mtp.plot(g,h)
mtp.show()

#LOOP
print("\n\nLoop all")
n = 3
i = 0
while i < n :
	print(d[i])
	i = i+1

for x in a :
	print(x) 

for x in range(5) :
	print(x) 

