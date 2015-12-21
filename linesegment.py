# intestazione
import uuid
from utils import *
import xml.dom.minidom
# fine intestazione

# global variables
linesegments_type = ['IMPLICIT','EXPLICIT']
# horizontal or vertical 
directions_type = ['H','V','O']
# threshold to consider if it is vertical or horizontal
point_vh_threshold = 20
# end global variables

class linesegment(object) :

	def __init__(self, points, mytype = None, myclass = None, features = none, uid = None) :
		'''
		A linesegment. Has a list of points.
		'''
		global linesegments_type
		global directions_type
		global point_vertical_threshold

		if not uid :
			self.id = getId()
		else 
			self.id = uid

		if type(points) is list :
			self.points = points 
			if len(self.points) != 2 :
				print "Lingesegment not composed by two points - possible errors"
		else :
			# TODO - come gestire gli errori?
			pass

		if mytype in linesegments_type :
			self.type = mytype 
		else :
			#TODO - come gestire gli errori?
			pass

		self.myclass = myclass
		self.features = features 

		self.direction = str()
		p1 = self.points[0]
		p2 = self.points[1]
		#TODO CHECK
		if abs(p1[0]**2 +p2[0]**2) < point_vertical_threshold :
			self.direction = ['H']
		elif abs(p1[1]**2 +p2[1]**2) < point_vertical_threshold :
			self.direction = ['O']
		else :
			self.direction = ['V']

	def tostr(self) : 
		pass

	def toxml(self) :
		pass

	def metodi_vari(self) :







