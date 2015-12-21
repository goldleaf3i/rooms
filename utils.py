#!
import xml.dom.minidom
import xml.etree.ElementTree as ET
import uuid
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx




def dict_to_xml(dictionary, doc):
	'''
	funziona con DOM
	receives a dictionary as {"a": 12, "b" : {"C":4,"D":'asda'}} and prints
	<a>
		12
	</a>
	<b>
		<c>4</c>
		<D>asda</D>
	</b>
	'''

	for i in dictionary.keys() :
		tmp = ET.SubElement(doc,str(i))
		if type(dictionary[i]) is dict :
			dict_to_xml(dictionary[i],tmp)
		else :
			tmp.text = str(dictionary[i])



def dict_to_xmlDOM(dictionary, doc, elem):
	'''
	funziona con DOM
	receives a dictionary as {"a": 12, "b" : {"C":4,"D":'asda'}} and prints
	<a>
		12
	</a>
	<b>
		<c>4</c>
		<D>asda</D>
	</b>
	'''

	for i in dictionary.keys() :
		tmp = doc.createElement(str(i))
		content = doc.createTextNode(str(dictionary[i]))
		if type(dictionary[i]) is dict :
			dict_to_xml(dictionary[i],doc,tmp)
		else :
			tmp.appendChild(content)
		elem.appendChild(tmp)


def getId(length = 6) :
	'''
	returns a uniqueID of size "length" characters
	'''
	return str(uuid.uuid4())[:length]

def separatePrintOut():
	print('*+' * 50)
	return

def printMatrix(M, sep = '') :
	# stampa a schermo una matrice.
	# M la matrice, sep il separatore es sep = ',' -> 3,4,5,6,7,8 
	retvalue = str()
	righe = len(M)
	colonne = len(M[0])
	print('*'*50)
	for x in xrange(colonne) :
		row = []
		temprow = str()
		for y in xrange(righe) :
			temp = str(M[x][y]) + sep
			temprow +=temp
		print(temprow)
		retvalue += temprow + "\n"
	print('*'*50)
	return retvalue

################################################# INIZIO FUNZIONI CHE GESTISCONO I COLORI #################################################

def get_list_of_colors(num_of_colors = 20, colormap = "Paired") :
	'''
	Questo metodo ti stampa un elenco di colori da una data colormap. 
	TODO bisogna 
	'''
	numofcolors = num_of_colors
	cm = plt.get_cmap(colormap)
	cNorm = colors.Normalize(vmin=0, vmax=numofcolors)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap = cm)
	for i in range(numofcolors) :
		print scalarMap.to_rgba(i)

	labelsdict = dict()
	numbersdict = dict()

	for i in range(numofcolors) : 
		labelsdict["N"+str(i)] = colors.rgb2hex(scalarMap.to_rgba(i))
		numbersdict["N"+str(i)] = i
	print "List of colors"
	for i in labelsdict :
		print "'"+str(i)+ "' : '" +  str(labelsdict[i]) +  "',"
	for i in numbersdict :
		print "'"+str(i)+ "' : "+ str(numbersdict[i]) + ","

	return {'labels':labelsdict, 'numbers':numbersdict}


def createColorDict(list_of_labels) :
	# crea un dizionario dove le chiavi sono una lista di labels, e il valore sono dei colori. Usa le colormap di matplotlib per farlo
	# qui sotto un esempio di come si estraggono dei colori dalle colormap.
	'''>>> color = np.random.random(10)
	>>> color
	array([ 0.75188924,  0.39101616,  0.76249589,  0.09931891,  0.55436453,
	        0.35272904,  0.46937771,  0.94932506,  0.01736672,  0.60044431])
	>>> aaaaa = cm.winter(color)
	>>> aaaaa
	array([[ 0.        ,  0.75294118,  0.62352941,  1.        ],
	       [ 0.        ,  0.39215686,  0.80392157,  1.        ],
	       [ 0.        ,  0.76470588,  0.61764706,  1.        ],
	       [ 0.        ,  0.09803922,  0.95098039,  1.        ],
	       [ 0.        ,  0.55294118,  0.72352941,  1.        ],
	       [ 0.        ,  0.35294118,  0.82352941,  1.        ],
	       [ 0.        ,  0.47058824,  0.76470588,  1.        ],
	       [ 0.        ,  0.95294118,  0.52352941,  1.        ],
	       [ 0.        ,  0.01568627,  0.99215686,  1.        ],
	       [ 0.        ,  0.6       ,  0.7       ,  1.        ]])
	>>> bb = cm.RdGy(color) 
	pp = [(x,0) for x in range(len(bb))]
	>>> for i in pp :
	...     ax.plot([i[0]],[i[1]], 'o',color = bb[i[0]])
	'''
	colors = dict()
	tmp_colors = getColorFromColorMap(len(list_of_labels))
	for i in range(len(list_of_labels)) :
		colors[str(list_of_labels(i))] = tmp_colors[i]
	return colors

def getColorFromColorMap(n_colors, colormap = None ):
	# prendo un numero x e un color_map name e restituisco un array di x colori appartenenti a colormap.
	# array da 1 a n_colors
	#lista dei colormaps di matplotlib. la copio qui se serve. sono i parametri accettati come "colormap"
	'''cmaps = [('Sequential',['Blues', 'BuGn', 'BuPu',
		'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
		'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
		'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
	 ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
		'gist_heat', 'gray', 'hot', 'pink',
		'spring', 'summer', 'winter']),
	 ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
		'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
		'seismic']),
	 ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
	 	'Pastel2', 'Set1', 'Set2', 'Set3']),
	 ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
		'brg', 'CMRmap', 'cubehelix',
		'gnuplot', 'gnuplot2', 'gist_ncar',
		'nipy_spectral', 'jet', 'rainbow',
		'gist_rainbow', 'hsv', 'flag', 'prism'])]'''
	tmp_array = np.array(range(n_colors))
	# se ho un colormap dato come parametro lo uso, altrimenti ne prendo a caso da un set.
	if colormap :
		t_cm = cm.get_cmap(colormap) 
	else :
		list_of_cmap = ['Accent', 'Dark2', 'Paired', 'Pastel1','Pastel2', 'Set1', 'Set2', 'Set3']
		cm_name = list_of_cmap[np.random.randint(0,len(list_of_cmap))]
		t_cm = cm.get_cmap(cm_name)
	#restituisce un numpy-array con n_colors colori.
	return t_cm(tmp_array)	

################################################# FINE FUNZIONI CHE GESTISCONO I COLORI #################################################