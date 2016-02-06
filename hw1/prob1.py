import numpy as np
from matplotlib import pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D

#first load all the data
data = np.loadtxt('iris_data.txt')
num_class = 3;
num_feature = 4;
data_class = []
for i in np.arange(num_class):
	data_class.append(data[data[:,4] == (i+1),:])

#prob1, draw the histogram of 4 features
num_bin = 10;
plot_color = ('red','green','blue');
for i in np.arange(num_feature):
	plt.figure()
	for j in np.arange(num_class):
		heights,edges = np.histogram(data_class[j][:,i],bins = num_bin)
		width = 0.7 * (edges[1]-edges[0])
		coordinates = (edges[:-1]+edges[1:])/2
		pdf = heights.astype(float)/np.sum(heights)
		plt.bar(coordinates, pdf, color = plot_color[j], width = width, label = 'Class %d'%(j+1))
	title_str = 'Histogram of feature %d'%(i+1)
	plt.xlabel('x%d'%(i+1))
	plt.title(title_str)
	plt.legend()
plt.show()

#prob2, draw the scatter plots of two different 2d feature combination
markers = ('x','_','^')
plt.figure()
#first feature(x1,x2)
plt.subplot(2,1,1)
for i in np.arange(num_class):
	data_cur = data_class[i]
	plt.scatter(data_cur[:,0], data_cur[:,1], marker = markers[i], label = 'Class %d'%(i+1), s = 40)
plt.title('feature (x1,x2)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc = 'lower right')
plt.show()

#then feature(x1,x4)
plt.subplot(2,1,2)
for i in np.arange(num_class):
	data_cur = data_class[i]
	plt.scatter(data_cur[:,0], data_cur[:,3], marker = markers[i], label = 'Class %d'%(i+1), s = 40)
plt.title('feature (x1,x4)')
plt.xlabel('x1')
plt.ylabel('x4')
plt.legend(loc = 'lower right')
plt.show()

#Prob 3
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
for i in np.arange(num_class):
	data_cur = data_class[i]
	ax.scatter(data_cur[:,0],data_cur[:,1],data_cur[:,3], marker = markers[i], label = 'Class %d'%(i+1), s = 40)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x4')
plt.title('feature (x1,x2,x4)')
plt.legend()
plt.show()
