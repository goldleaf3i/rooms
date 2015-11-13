# intestazione
import uuid
from utils import *
import xml.dom.minidom
# fine intestazione

class group(object) :

	def __init__(self, mytype,name, uid = None) :
		'''
		Group relation between multiple spaces. 

		Initially the relation is EMPTY

		Three possible types of group relation are possible:
		1: a group is a LIST of spaces 
		[space1, space2,space3, ...]
		2: a group is a LIST of LIST of spaces (e.g. all the rooms that have the SAME shape)
		[ [space 1, space2, space 3], [space3,space5,space6], [...]]
		3: a group is formed by a DICTIONARY of subGROUPS (as a list) [e.g., functional areas]
		{'corridor' = [space1,space2,space3],'corridor_2' =[space3,space4,space5]}

		PARAM: 
		mytype - the type of the relation 
		name - name of the relation
		e.g.
		mytype - "functional area"
		name - "entrance"


		QUESTA DIVISIONE E' TRASPARENTE - UN SOLO TIPO DI LISTA E' IMPLEMENTATO - RIPOTTARE IN FLOORS QUESTA COSA
		'''
		if not uid :
			self.id = getId()
		else 
			self.id = uid

		# type of the (group) relation. The group relations of the same type should be consired altogether.
		self.type = mytype 
		# name of the relation.
		self.name = name 
		# list of spaces which are in relation between them
		self.spaces = []
		# OPTIONAL a dictionary of attributes that belongs to the relation
		self.attributes = dict()
		# OPTIONAL a string that describes the relation 
		self.description = str()
		# xml representation
		self.xml = None

	def add(self, obj) :
		# adds an object to the relation
		self.space.append(obj)

	def addAttribute(self,name,value) :
		# adds an attribute
		self.attributes[name] = value

	def setDescription(self,description) :
		# setter
		selt.description = description 

	def toxml(self, doc,elem):
		# append an xml description to a XML file
		pass