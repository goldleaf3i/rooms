#!/usr/bin/python
from rooms import *
from utils import *
from myDictionaries import * 
# Qui ci vanno le funzioni che si usano per caricare (e salvare?) i grafi.

# COPIATO DA CARTELLLA DI SVILUPPO 15/9/14

def loadXML():
	pass

def loadOldJava():
	# questo mi sa che mi conviene farlo a mano in MapToXML
	pass

def loadGSpan():
	pass

def loadAdiacencyMatlabToTopological(matrix,labels_dict,labelsRC_dict = None , colors = None):
	# parametri: una matrice di adiacenza, un dizionario per convertire in label il valore numerico della diagonale
	# un dizionario per convertire le label appena ottenute in R o C e un dizionario dei colori delle label
	m = matrix 
	rows = len(matrix)
	columns = len(matrix[0])
	node_id_list = [str(i) for i in range(rows)]
	labels = []
	labelRC = []
	edge_list = []
	special_edge = []
	for i in range(rows) :
		for j in range(columns) :
			if i == j :
				labels.append( labels_dict[m[i][j]] )
				if labelsRC_dict :
					labelRC.append( labelsRC_dict( labels_dict[m[i][j]] ) ) 
			else :
				if m[i][j] == 1 :
					edge_list.append( ( i,j) )
				if m[i][j] == 2 :
					special_edge.append( (i,j) )

	if labelRC :
		topological_map = topologicalMap(node_id_list, labels, labelsRC, edge_list, colors )
	else :
		topological_map = topologicalMap(node_id_list,labels, edge_list = edge_list, colors = colors )
	#if special_edge != [] :
	#	topological_map.add_special_edge_list(special_edge)
	return topological_map

def importFromMatlabJava2012FormatToIgraph(matrix, RC = False, nolabel = False  ) :
	# funzione che prende una matrice di adiacenza fatta usando come dati i miei di del 2012 e poi li importa in importFromMatlabJava2012FormatToIgraph
	# Se RC e' True passo anche le variabili bipartite R-C oltre che le altre variabili.
	# se nolabel e' true sostituisco alle label R o C (3 o 100) a seconda del degree. 
	if nolabel :
		rows = len(matrix) 
		for i in range(rows) :
			for j in range(rows) :
				tmp = sum(matrix[i])
				if tmp >= 3 :
					matrix[i][i] = labels_java2012toMatlab_Dict['C']
				else :
					matrix[i][i] = labels_java2012toMatlab_Dict['M']

	reverse_java_matrix_dict = dict()
	labels = labels_java2012toMatlab_Dict
	for i in labels.keys():
		reverse_java_matrix_dict[labels[i]] = i
	if RC: 
		mygraph = loadAdiacencyMatlabToTopological(matrix,reverse_java_matrix_dict,labels_RC_java2012, Java2012_colorDict)
	else : 
		mygraph = loadAdiacencyMatlabToTopological(matrix,reverse_java_matrix_dict, colors = Java2012_colorDict)
	return mygraph

def myT(A,B,C) :
	return importFromMatlabJava2012FormatToIgraph(A,B,C)
	