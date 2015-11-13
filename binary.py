# intestazione
import uuid
from utils import *
import xml.dom.minidom
# fine intestazione

class binary(object) :

	def __init__(self, space1, space2, mytype,name, uid = None) :	
		'''
		Binary relation between two spaces. 

		Initially the relation receives two spaces

		DOMANDA: che differenza c'è tra BINARY e GROUP?
		'''
		if not uid :
			self.id = getId()
		else 
			self.id = uid

		# type of the relation. Relations of the same type should be consired altogether.
		self.type = mytype 
		# name of the relation.
		self.name = name 
		# list of spaces which are in relation between them
		self.spaces = [space1, space2]
		# OPTIONAL a dictionary of attributes that belongs to the relation
		self.attributes = dict()
		# OPTIONAL a string that describes the relation 
		self.description = str()
		# xml representation
		self.xml = None

	def addAttribute(self,name,value) :
		# adds an attribute
		self.attributes[name] = value

	def setDescription(self,description) :
		# setter
		selt.description = description 

	def toxml(self, doc,elem):
		# append an xml description to a XML file
		pass