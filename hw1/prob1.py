import numpy as np
from matplotlib import pyplot as plt

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
		plt.bar(coordinates, pdf, color = plot_color[j], width = width)
	
plt.show()

