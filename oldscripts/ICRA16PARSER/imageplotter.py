import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
#from scipy.misc import imread
import matplotlib.cbook as cbook
import numpy as np
import math
import cmath
import glob

functional_labels=["CONFERENCE ROOM","CUBICLE","OFFICE","SHARED OFFICE","EXECUTIVE OFFICE","CONFERENCE HALL","OPENSPACE","SMALL","MEDIUM","CLASSROOM","LAB"]
# CHECK I TODO 


###ADDING FEATURES###

#dataset
#SOLO CORR NO LABEL
buildingtypestr = str()
#TUTTE LE LABEL
buildingtypestr2 = str()
#SOLO ALCUNE LABEL
buildingtypestr3 = str()
# 4 LABEL (R/C/E/S)
buildingtypestr4 = str()
# 2 label (R/C)
buildingtypestr5 = str()

for dataset_name in ["office","school"] :
#dataset_name = "office"
#	for xml_file in glob.glob('Input/'+dataset_name+'/*.xml'):
	if True :
		xml_file = 'test.xml'
		print xml_file
		#xml_name = xml_file[6:]
		xml_name = xml_file
		print xml_name
		tree = ET.parse(xml_file)
		root = tree.getroot()
		floor = root.find('floor')
		spaces = floor.find('spaces')
		pixels = int(root.find('scale').find('represented_distance').find('value').text)

		for space in spaces.iter('space'):
			points = []
			area = 0
			perimeter = 0
			DCS = []
			for point in space.find('bounding_polygon').findall('point'):
				points += [[int(point.get('x'))/pixels,int(point.get('y'))/pixels]]
			centxml = space.find('centroid').find('point')
			cent = [int(centxml.get('x'))/pixels,int(centxml.get('y'))/pixels]
			print points
			
			#legacy: for plotting
			poly = plt.Polygon(points, closed=True, fill=None, edgecolor='r')
			plt.gca().add_patch(poly)
			plt.plot([1,2,3,4], [1,4,9,16], 'ro')

			#MISSING FEATURES:
			#For 6 7 8
			#complex_points = []
			#for e in points:
			#	complex_points.append(complex(e[0],e[1]))
			#print complex_points
			#fftarray = np.fft.fft(complex_points)	
			# 9 10 11 MISSING
			
		
			
		#legacy: linesegment plot for comparison
		for space in spaces.iter('space'):
			for lineseg in space.find('space_representation').findall('linesegment'):
				points = []
				for point in lineseg.findall('point'):
					points += [int(point.get('x'))]
					points += [int(point.get('y'))]
				line = plt.Line2D((points[0], points[2]), (points[1], points[3]), lw=0.5, markerfacecolor='b', markeredgecolor='b')
				plt.gca().add_line(line)
		
		#indent(root)
		#tree.write('Output/XMLs/'+xml_name)
	img = imread('c.jpg')
	plt.imshow(img)
	plt.axis('image')
	plt.axis('off')
	plt.show()
	exit()
	###END ADDING FEATURES###

	#legacy: using topological xml
	
	tree = ET.parse('b.xml')
	root = tree.getroot()
	nodes = root.find('nodes')

	for node in nodes.iter('node'):
		rgbcol = []
		rgbcol += [float(node.find('color').get('r'))/255,float(node.find('color').get('g'))/255,float(node.find('color').get('b'))/255]
		nodecolor = pltcol.rgb2hex(rgbcol)
		
	connections = root.find('connections')
	for connection in connections.iter('connection'):
		ids = connection.findall('id')
		#print "interpretation(test,connected("+nodes_dict[int(ids[0].text)][0]+","+nodes_dict[int(ids[1].text)][0]+"))."
		myglobalstr += "interpretation(test,connected("+nodes_dict[int(ids[0].text)][0]+","+nodes_dict[int(ids[1].text)][0]+")).\n"
		line = plt.Line2D((nodes_dict[int(ids[0].text)][3], nodes_dict[int(ids[1].text)][3]), (nodes_dict[int(ids[0].text)][4], nodes_dict[int(ids[1].text)][4]), lw=0.5)
		plt.gca().add_line(line)
	'''


	for xml_file in glob.glob('Output/XMLs/'+dataset_name+'/*.xml'):
		tree = ET.parse(xml_file)
		root = tree.getroot()
		floor = root.find('floor')
		spaces = floor.find('spaces')
		interpretation = 'i'+(xml_file[12:]).translate(None, '/').translate(None, ' ').translate(None, '-').translate(None, '.')

		for space in spaces.iter('space'):
			#General info
			name = space.get('id')
			kname = 'r'+name[:6].translate(None, '.').translate(None, '-').translate(None, ' ')
			label = space.find('labels').find('label').text
			klabel = 'l'+label.lower().translate(None, '/').translate(None, ' ').translate(None, '-')
			myglobalstr += "interpretation("+interpretation+",room("+kname+")).\n"
			
			#Features

			#Connections
			for portal in space.find('portals').findall('portal'):
				involved = []
				for i in portal.find('target').findall('id'):
					involved += [i.text]
				source = involved[0]
				destination = involved[1]
	
			
			#Labels
			



			#legacy for plotting
			circle = plt.Circle((nodes_dict[i][3], nodes_dict[i][4]), radius=10, fc=nodes_dict[i][5])
			plt.gca().add_patch(circle)

#legacy for plotting

img = imread('c.jpg')
plt.imshow(img)
plt.axis('image')
plt.axis('off')
plt.show()
plt.savefig('test.jpg')
plt.savefig('test.jpg', dpi=xxx)
'''

