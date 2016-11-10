#### Using Python 2.7
#### By Wei Zou



import numpy as np 
import matplotlib.pyplot as plt
import itertools as it
from collections import Counter


##################################################################### 

# generate the corners of the hypercube
D = input('Enter the dimension of the hypercube: ') # try 10, 100, 1000


def compute_angle(point1,point2):
	#since the unit length must be sqrt(D)
	return np.dot(point1,point2)/(np.linalg.norm(point1)*np.linalg.norm(point2))

N = 100000 # randomly select 10000 pairs

# generate the pairs and calcuate the angle btw each pair
results = np.zeros(N)
i=0
while(i < N):
	points_pre = np.random.rand(2,D) # generate 2*D array
	points_pre[points_pre<=0.5] = -1
	points_pre[points_pre>0.5] = 1
	results[i] = compute_angle(points_pre[0],points_pre[1])
	i = i+1



print 'min is '
print min(results)
print 'max is '
print max(results)
print 'range is '
print max(results)-min(results)
print 'mean is '
print np.mean(results)
print 'variance is '
print np.var(results)


plt.hist(results, bins=50, normed=True)
plt.show()



'''

