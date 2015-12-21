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

def find_area (array):
	a = 0
	ox,oy = array[0]
	for x,y in array[1:]:
		a += (x*oy-y*ox)
		ox,oy = x,y
	return abs(a/2)

def find_perimeter (array):
	p = 0
	ox,oy = array[0]
	for x,y in array[1:]:
		p += points_distance(ox,oy,x,y)
		ox,oy = x,y
	return p
	
def dist_centr_bound(c,array):
	val = []
	cx,cy = c
	for x,y in array[1:]:
		val += [points_distance(cx,cy,x,y)]
	return val

def normalize_array(array):
	maxval = np.amax(array)
	for i in range(len(array)):
		array[i] = array[i]/maxval
	return array
	
def points_distance (x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

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
	for xml_file in glob.glob('Input/'+dataset_name+'/*.xml'):
		print xml_file
		xml_name = xml_file[6:]
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
			area = find_area (points)
			perimeter = find_perimeter (points)
			DCS = dist_centr_bound(cent,points)
			
			#legacy: for plotting
			#poly = plt.Polygon(points, closed=True, fill=None, edgecolor='r')
			#plt.gca().add_patch(poly)
			
			#MISSING FEATURES:
			#For 6 7 8
			#complex_points = []
			#for e in points:
			#	complex_points.append(complex(e[0],e[1]))
			#print complex_points
			#fftarray = np.fft.fft(complex_points)	
			# 9 10 11 MISSING
			
			features_xml = ET.SubElement(space, 'features')
			
			area_xml = ET.SubElement(features_xml,'area')
			area_xml.set('value', str(area))

			perimeter_xml = ET.SubElement(features_xml,'perimeter')
			perimeter_xml.set('value', str(perimeter))

			f3_xml = ET.SubElement(features_xml,'aoverp')
			f3_xml.set('value', str(area/perimeter))

			f4_xml = ET.SubElement(features_xml,'adcs')
			f4_xml.set('value', str(np.mean(DCS)))

			f5_xml = ET.SubElement(features_xml,'Standard_Deviation_Dist_Cent-Shape')
			f5_xml.set('value', str(np.std(DCS)))

			f12_xml = ET.SubElement(features_xml,'ff')
			f12_xml.set('value', str(4*math.pi*area/math.sqrt(perimeter)))

			f13_xml = ET.SubElement(features_xml,'circularity')
			f13_xml.set('value', str(perimeter**2/area))

			f14_xml = ET.SubElement(features_xml,'normalcirc')
			f14_xml.set('value', str(4*math.pi*area/perimeter**2))

			f15_xml = ET.SubElement(features_xml,'andcs')
			f15_xml.set('value', str(np.mean(normalize_array(DCS))))

			f16_xml = ET.SubElement(features_xml,'Standard_Deviation_Dist_Cent-Shape')
			f16_xml.set('value', str(np.std(normalize_array(DCS))))
			
		#legacy: linesegment plot for comparison
		'''for space in spaces.iter('space'):
			for lineseg in space.find('space_representation').findall('linesegment'):
				points = []
				for point in lineseg.findall('point'):
					points += [int(point.get('x'))]
					points += [int(point.get('y'))]
				line = plt.Line2D((points[0], points[2]), (points[1], points[3]), lw=0.5, markerfacecolor='b', markeredgecolor='b')
				plt.gca().add_line(line)'''

		indent(root)
		tree.write('Output/XMLs/'+xml_name)

	###END ADDING FEATURES###

	#legacy: using topological xml
	'''
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

	###FROM XML TO KLOG###
	myglobalstr = str()
	alphastring = str()
	betastr = str()
	gammastr = str()
	xstr = str()
	ystr = str()
	duestr = str()
	trestr = str()
	zetastr = str()
	omegastr = str()
	sigmastr = str()
	nustr = str()

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
			features_xml = space.find('features')
			area = features_xml.find('area').get('value')
			perimeter = features_xml.find('perimeter').get('value')
			aoverp = features_xml.find('aoverp').get('value')
			adcs = features_xml.find('adcs').get('value')
			ff = features_xml.find('ff').get('value')
			circularity = features_xml.find('circularity').get('value')
			normalcirc = features_xml.find('normalcirc').get('value')
			andcs = features_xml.find('andcs').get('value')
			myglobalstr += "interpretation("+interpretation+",area("+kname+","+area+")).\n"
			myglobalstr += "interpretation("+interpretation+",perimeter("+kname+","+perimeter+")).\n"
			myglobalstr += "interpretation("+interpretation+",aoverp("+kname+","+aoverp+")).\n"
			myglobalstr += "interpretation("+interpretation+",adcs("+kname+","+adcs+")).\n"
			myglobalstr += "interpretation("+interpretation+",ff("+kname+","+ff+")).\n"
			myglobalstr += "interpretation("+interpretation+",circularity("+kname+","+circularity+")).\n"
			myglobalstr += "interpretation("+interpretation+",normalcirc("+kname+","+normalcirc+")).\n"
			myglobalstr += "interpretation("+interpretation+",andcs("+kname+","+andcs+")).\n"
			
			#Connections
			for portal in space.find('portals').findall('portal'):
				involved = []
				for i in portal.find('target').findall('id'):
					involved += [i.text]
				source = involved[0]
				destination = involved[1]
				myglobalstr += "interpretation("+interpretation+",connected(r"+source[:6].translate(None, '.').translate(None, '-').translate(None, ' ')+",r"+destination[:6].translate(None, '.').translate(None, '-').translate(None, ' ')+")).\n"		
			
			#Labels
			
			#alpha&uno
			# TODO ERRORE CORRIDOR E ROOM NON SONO COSI' 
			if label == 'CORRIDOR' or label =='HALL' or label =='LOBBY' :
				alphastring += "interpretation("+interpretation+",corr("+kname+")).\n"
				omegastr+=  "interpretation("+interpretation+",label("+kname+",lcorridor)).\n"
				nustr += "interpretation("+interpretation+",label("+kname+",lcorridor)).\n"
			elif label == "ENTRANCE" or label == "ELEVATOR" or label == "STAIRS":
				omegastr+=  "interpretation("+interpretation+",label("+kname+",lentrance)).\n"
				nustr += "interpretation("+interpretation+",label("+kname+",lroom)).\n"
			else:
				omegastr+=  "interpretation("+interpretation+",label("+kname+",lroom)).\n"
				nustr += "interpretation("+interpretation+",label("+kname+",lroom)).\n"

			#beta
			if (label =='CORRIDOR' or label =='CLASSROOM' ):
				betastr += "interpretation("+interpretation+",label("+kname+","+klabel+")).\n"
			else:
				betastr += "interpretation("+interpretation+",label("+kname+",lother)).\n"
			
			#gamma		
			gammastr += "interpretation("+interpretation+",label("+kname+","+klabel+")).\n"
			
			#x
			if (label =='CORRIDOR' or label =='CLASSROOM' or label =='BATHROOM'):
				xstr += "interpretation("+interpretation+",label("+kname+","+klabel+")).\n"
			else:
				xstr += "interpretation("+interpretation+",label("+kname+",lother)).\n"
			
			#y
			if label == 'CORRIDOR':
				ystr += "interpretation("+interpretation+",corr("+kname+")).\n"
			elif label == 'CLASSROOM':
				ystr += "interpretation("+interpretation+",class("+kname+")).\n"
			elif label == 'BATHROOM':
				ystr += "interpretation("+interpretation+",bath("+kname+")).\n"
			
			#due
			if label == 'CLASSROOM':
				duestr += "interpretation("+interpretation+",class("+kname+")).\n"
			
			#tre
			if label == 'BATHROOM':
				trestr += "interpretation("+interpretation+",bath("+kname+")).\n"
			
			if label == 'CORRIDOR' or label =='HALL' or label =='LOBBY' :
				sigmastr+=  "interpretation("+interpretation+",label("+kname+",lcorridor)).\n"
			elif label == "ENTRANCE" or label == "ELEVATOR" or label == "STAIRS":
				sigmastr+=  "interpretation("+interpretation+",label("+kname+",lentrance)).\n"
			elif label in functional_labels :
				sigmastr+=  "interpretation("+interpretation+",label("+kname+",lroom)).\n"
			else:
				sigmastr+=  "interpretation("+interpretation+",label("+kname+",lservice)).\n"



			#legacy for plotting
			#circle = plt.Circle((nodes_dict[i][3], nodes_dict[i][4]), radius=10, fc=nodes_dict[i][5])
			#plt.gca().add_patch(circle)
		zetastr += "interpretation("+interpretation+",flabel("+dataset_name+")).\n"
	buildingtypestr += myglobalstr + alphastring + zetastr
	buildingtypestr2 += myglobalstr + gammastr + zetastr
	buildingtypestr3 += myglobalstr + omegastr + zetastr
	buildingtypestr4 += myglobalstr + sigmastr + zetastr
	buildingtypestr5 += myglobalstr + nustr + zetastr

	text_file = open('Output/'+dataset_name+'/alpha_s_ext.pl', "w")
	text_file.write(myglobalstr+alphastring)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/uno_ext.pl', "w")
	text_file.write(myglobalstr+alphastring)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/beta_s_ext.pl', "w")
	text_file.write(myglobalstr+betastr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/gamma_s_ext.pl', "w")
	text_file.write(myglobalstr+gammastr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/x_s_ext.pl', "w")
	text_file.write(myglobalstr+xstr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/y_s_ext.pl', "w")
	text_file.write(myglobalstr+ystr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/due_ext.pl', "w")
	text_file.write(myglobalstr+duestr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/tre_ext.pl', "w")
	text_file.write(myglobalstr+trestr)
	text_file.close()
	text_file = open('Output/'+dataset_name+'/tre_ext.pl', "w")
	text_file.write(myglobalstr+trestr)
	text_file.close()
	# PHI: 3 LABEL - CORRIDOR - ROOM - ENTRANCE
	text_file = open('Output/'+dataset_name+'/phi_ext.pl', "w")
	text_file.write(myglobalstr+omegastr)
	text_file.close()
	# SIGMA: 4 LABEL - CORRIDOR - ROOM - ENTRANCE - SERVICE
	text_file = open('Output/'+dataset_name+'/sigma_ext.pl', "w")
	text_file.write(myglobalstr+sigmastr)
	text_file.close()
	# NU: 2 LABEL - CORRIDOR - ROOM.
	text_file = open('Output/'+dataset_name+'/nu_ext.pl', "w")
	text_file.write(myglobalstr+nustr)
	text_file.close()
	###END OF TRANSLATION###

# NO LABEL - ONLY CORR + INTERPRETATION
print buildingtypestr
text_file = open('Output/zeta_ext.pl', "w")
text_file.write(buildingtypestr)
text_file.close()
# ALL LABELS + INTERPRETATION
text_file = open('Output/full_ext.pl', "w")
text_file.write(buildingtypestr2)
text_file.close()
# 3 LABELS : CORR - ROOM - ENTRANCE + INTERPRETATION
text_file = open('Output/omega_ext.pl', "w")
text_file.write(buildingtypestr3)
text_file.close()
# 4 LABELS : CORR - ROOM - ENTRANCE - SUPPORT + INTERPRETATION
text_file = open('Output/sigma_ext.pl', "w")
text_file.write(buildingtypestr4)
text_file.close()

# 2 LABELS : CORR - ROOM  + INTERPRETATION
text_file = open('Output/nu_ext.pl', "w")
text_file.write(buildingtypestr5)
text_file.close()

#legacy for plotting
'''
img = imread('c.jpg')
plt.imshow(img)
plt.axis('image')
plt.axis('off')
plt.show()
plt.savefig('test.jpg')
plt.savefig('test.jpg', dpi=xxx)
'''
