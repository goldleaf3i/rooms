#!/usr/bin/python

# COPIATO DA CARTELLLA DI SVILUPPO 15/9/14

from sys import argv
import re
import sys
import math
from loadGraph import *
'''
M = [[1,1,1,0,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,0,0,0,0,0],
[0,1,0,1,1,1,0,0],
[0,0,0,1,1,1,1,1],
[0,0,0,1,1,1,0,0],
[0,0,0,0,1,0,1,1],
[0,0,0,0,1,0,1,1]]
funziona = myT(M,False,True)
#funziona = importFromMatlabJava2012FormatToIgraph(matrice, True)
'''
nome = "./testEdifici/adiacenza+label_Mappa_Scuole_";
i = 3;
stringa = str();
padding = str();
try:
	while True:
		if i < 10:
			padding = "000"
		elif i < 100:
			padding = "00"
		else :
			padding = "0"
		filename = nome + padding + str(i);
		
		myfile = open(filename+".txt");
		matrix = []
		for line in myfile:
			#rimuovo le cose in eccesso
			line = line.replace('[','')
			line = line.replace(';','')
			line = line.replace(']','')
			matrix.append([int(j)for j in line.split(',')])
		myfile.close()
		topologicalmap = importFromMatlabJava2012FormatToIgraph(matrix)
		graph = topologicalmap.graph
		plot(graph,filename+".png")
		print "ho finito con " + filename 
		print i
		print type(i)
		i+=1
		print i
except Exception as e: print(e)

