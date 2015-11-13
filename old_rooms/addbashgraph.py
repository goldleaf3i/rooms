#!/usr/bin/python

# QUESTO SCRIPT CARICA IL GRAFO DI DEFAULT NEL TERMINALE PER FARLO USARE IN MANIERA INTERATTIVA E TESTARE LE COSE
from sys import argv
import re
import sys
import math
import numpy as np
from matplotlib import pyplot 
from shapely.geometry import LineString
from roomfloorplans import *
from utils import *
import uuid
from igraph import *
from random import *


room_file_name = "dataset_stanze_ufficio.txt"
integerDict = {'C': 100,'S': 2,'H':105,'B':4,'M':3,'E':1000,'R':5,'F':6, 'N':7,'D':8, 'O':1, 'K':0, "|":10000}	
colorDict = {'C':'#0BFF12','S':'#FFF40F','H':'#4DF5FF','B':'#CC1900','M':'#FFBB00','E':'#341FB2','R':'#FFB955','F':'#973CFF', 'N':'#1BCC50','D':'#6118B2', 'O':'#E8A90C', 'K':'#0DFFAF', "|":"#FF0DFF"}
# SOLITO GRAFO DI TEST
numofvx = 36
node_label_dict = {
"0": "R",
"1": "C",
"2": "C",
"3": "C",
"4": "C",
"5": "C",
"6": "C",
"7": "C",
"8": "C",
"9": "C",
"10": "R",
"11": "R",
"12": "R",
"13": "R",
"14": "R",
"15": "R",
"16": "R",
"17": "R",
"18": "R",
"19": "R",
"20": "R",
"21": "R",
"22": "R",
"23": "R",
"24": "R",
"25": "E",
"26": "E",
"27": "R",
"28": "R",
"29": "C",
"30": "R",
"31": "R",
"32": "R",
"33": "R",
"34": "R",
"35": "R"}
edges_dict = {
"0": [],
"1": [33,10,11,12,13,2,0,8],
"2": [14,15,3,9],
"3": [16,17,18,19,4,20],
"4": [5],
"5": [20,21,22,23,24,6],
"6": [9,25,26,7],
"7": [27,0,8,33,28,29],
"8": [34,35],
"9": [],
"10": [],
"11": [],
"12": [],
"13": [],
"14": [],
"15": [],
"16": [],
"17": [],
"18": [],
"19": [],
"20": [],
"21": [],
"22": [],
"23": [],
"24": [],
"25": [],
"26": [],
"27": [],
"28": [29],
"29": [30],
"30": [31],
"31": [32],
"32": [],
"33": [],
"34": [],
"35": []}
node_full_label_dict = {
"0": "K",
"1": "C",
"2": "C",
"3": "C",
"4": "C",
"5": "C",
"6": "C",
"7": "C",
"8": "C",
"9": "H",
"10": "M",
"11": "M",
"12": "S",
"13": "S",
"14": "M",
"15": "M",
"16": "M",
"17": "M",
"18": "R",
"19": "S",
"20": "K",
"21": "S",
"22": "M",
"23": "S",
"24": "M",
"25": "E",
"26": "E",
"27": "S",
"28": "M",
"29": "C",
"30": "O",
"31": "K",
"32": "S",
"33": "K",
"34": "S",
"35": "S"}


def plot_graph_pyplot(len_graph,layout,colors,save = False) :
	node_poses = []
	for i in range(len_graph) :
		node_poses.append(layout[i])
	x,y = zip(*node_poses)
	scale_factor = 10

	print node_poses

	## STAMPO CON PYPLOT
	fig, ax = pyplot.subplots()

	for j in edgelist :
		x1 = x[j[0]]
		x2 = x[j[1]]
		y1 = y[j[0]]
		y2 = y[j[1]]
		ax.plot([x1,x2],[y1,y2],"k-")
	for i in range(len(x)) :
		ax.plot([x[i]],[y[i]],'o', color = colors[i])
	#ax.plot(x, y,'o')
	ax.grid(True)
	if not save :
		pyplot.show()
	else :
		pyplot.savefig( str(uuid.uuid4()) + '_.png', bbox_inches=0)
		pyplot.clf()

def special_plot(len_graph,layout,name,indexes,save = False):
	node_poses = []
	for i in range(len_graph) :
		node_poses.append(layout[i])
	x,y = zip(*node_poses)
	scale_factor = 10

	print node_poses

	## STAMPO CON PYPLOT
	fig, ax = pyplot.subplots()

	for j in edgelist :
		x1 = x[j[0]]
		x2 = x[j[1]]
		y1 = y[j[0]]
		y2 = y[j[1]]
		ax.plot([x1,x2],[y1,y2],"k-")
	for i in range(len(x)) :
		ax.plot([x[i]],[y[i]],'o', color = 'r' if i in indexes else 'k')
	#ax.plot(x, y,'o')
	ax.grid(True)
	if not save :
		pyplot.show()
	else :
		pyplot.savefig( name + '_.png', bbox_inches=0)
		pyplot.clf()



# GRAFO - qui parte da cambiare
# GRAFO QUI AGGIUNGO EDGELIST
g = Graph()
g.add_vertices(numofvx)
edgelist = []
for i in range(numofvx-1) :
	for j in edges_dict[str(i+1)] :
		edgelist.append( ( int(i+1),j))
		if not  i+1 in edges_dict[str(j)] :
			edges_dict[str(j)].append(int(i+1))
print edgelist
g.add_edges(edgelist)

#labels = [ node_label_dict[i] for i in node_label_dict.keys() ]
labels = [ node_label_dict[str(i)] for i in range(numofvx) ]
all_labels = [node_full_label_dict[str(i)] for i in range(numofvx)]
g.vs["room_label"]=labels
g.vs["label"]=g.vs["room_label"]
g.vs["all_label"]=all_labels
colors = [colorDict[label] for label in g.vs["label"]]
g.vs["color"] = colors 
layout = g.layout("kamada_kawai")

def default_print() :
	plot_graph_pyplot(numofvx,layout,colors,False)

print "you loaded the default graph. it has " + str(len(g.vs())) + " nodes"
print "it is in the variable 'g'"
print g
print "its layout is inside 'layout'"
print "you can plot it using 'default_print()'"
print "its attributes are 'room_label' (or alias 'label') 'all_label' and 'color' "
