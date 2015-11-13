# intestazione
import uuid
from utils import *
import xml.dom.minidom
# fine intestazione

connection_type = ["IMPLICIT", "EXPLICIT"]
class connection(object) :

	def __init__(self, space1, space2, mytype,uid = None) :	
		'''
		Binary relation between two spaces. 

		Initially the relation receives two spaces

		DOMANDA: che differenza c'è tra BINARY e GROUP?
		'''
		if not uid :
			self.id = getId()
		else 
			self.id = uid

		global connection_type
		if not mtype in connection_type :
		 	#TODO RAISE ERROR		
		# type of the (group) relation. The group relations of the same type should be consired altogether.
		self.type = mytype 
		# list of spaces which are in relation between them
		self.spaces = [space1, space2]
		# OPTIONAL a dictionary of attributes that belongs to the relation. INIT as default
		self.attributes = {'class' :'HORIZONTAL', 'direction' : 'BOTH'}
		# OPTIONAL a string that describes the relation 
		self.description = str()
		# xml representation
		self.xml = None

	def hasSpace(self,space) :
		return space in self.spaces 

	def addAttribute(self,name,value) :
		# adds/sets an attribute
		self.attributes[name] = value

	def setDescription(self,description) :
		# setter
		selt.description = description 

	def toxml(self, doc,elem):
		# append an xml description to a XML file
		pass