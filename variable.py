import numpy as np
from matplotlib import pyplot
from shapely.geometry import LineString
from descartes.patch import PolygonPatch
from igraph import *

class variable(object):
	# TODO COMMENTARE 
	# TODO AGGIUNGERE STAMPA SU FILE E COSE SIMILI
	def __init__(self,name = None):
		self.name = name
		self.campioni = list()
		self.n = 0
		self.media  = float(0)
		self.varianza = float(0)
		self.median = 0
		self.MAD = float()
		
	def add(self, x):
		self.campioni.append(x)
		self.n += 1
		
	def mean(self):
		self.media = 0
		for i in self.campioni:
			self.media += float(i)
		self.media /= float(self.n)
		return self.media
	
	def var(self):	
		for j in self.campioni:
			self.varianza += pow(float(j) - self.media , 2)
		self.varianza /= float(self.n - 1)
		return self.varianza
		
	def mad(self):
		floList = list()
		for i in self.campioni:
			floList.append(float(i))
		floList.sort()
		a = list()
		l = len(self.campioni)
		self.median = float(floList[int(l/2)])
		for i in floList:
			a.append(i-self.median if i-self.median > 0 else self.median-i)
		a.sort()
		self.MAD = a[int(l/2)]
		return self.MAD
		
	def printVariable(self):
		self.mean()
		self.var()
		self.mad()
		if self.name :
			a = 'variable: ' + str(self.name) + "\n"
		else :
			a = str()
		a += "la media risulta: " + str(self.media) + " e la deviazione standard invece: " + str(math.sqrt(self.varianza)) + "\n"
		a += "la varianza invece era: " + str( self.varianza ) + "\n"
		a += "il valore mediano era invece " + str( self.median ) + " e il MAD: " + str(self.MAD) + "\n"
		return a + "questo su " + str(self.n) + " campioni\n"	
			
#implementa una variabile intera dove conteggia il numero di cose
class integerVariable(object):

	def __init__(self):
		self.conteggio = dict()
		self.probabilita = dict()
		self.n = 0
		
	def add(self, x):
		self.n+=1
		if not(self.conteggio.has_key(x)) :
			self.conteggio[x] = 1
		else :
			self.conteggio[x] += 1
		
	def calcProbability(self):
		for i in self.conteggio.keys():
			self.probabilita[i] = float(self.conteggio[i]) / float(self.n)
			
	def printVariable(self):
		if self.n > 0:
			self.calcProbability()
		return str(self.probabilita)+ "\n"
