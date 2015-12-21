#!/usr/bin/env python

import matplotlib.pyplot as plt

formati = ['pr','roc','spr']

for f in formati:
	x = []
	y = []
	fig = plt.figure()
	ax = fig.add_subplot(111)
	xy = [float(i)/100 for i in range(0,101)]
	filename = 'output.yyy.'+f;
	myfile = open(filename)
	for i in myfile:
		print i
		x += [i.split()[0]]
		y += [i.split()[1]]
	ax.plot(x,y,'r-', xy,xy,'b--')
	plt.axis([-0.1,1.1,-0.1,1.1])
	fig.savefig(f+".png")
	#plt.show()