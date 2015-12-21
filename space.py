# intestazione
import uuid
from utils import *
import xml.dom.minidom
# fine intestazione

class space(object) :

	def __init__(self, label, space_representation = None, bounding_polygon = None, portals = None, boundingbox = None, centroid = None ) :
		"""
		"""

		# building_type è il nome del file da cui devo prendere l'xml oppure già l'xml

		# connections e' il secondo piu importante, gestisce le connessioni
		self.connections = []
		self.name = str()
		# scala dell'edificio /pixel vs metri / - e' un xml
		self.scale = dict()
		# chiave : campo; valore: valore del campo (anche stringa o dict) | e' un xml 
		self.info = dict()
		# chiave: campo; valore: ...
		self.building_type = dict()
		# bounding box - maxx maxy minx miny - sono quattro punti
		self.bounding_box = {
			'minx' : None,
			'maxx' : None,
			'minx' : None,
			'miny' : None
		}
		# contorno - potrebbe non esserci, e' un elenco (ordinato di punti)
		self.boundingpoly = space_representation
		# lista di linesegments del contonro - potrebbe non esserci - e' un dizionario
		self.linesegments = []
		# lista di porte che danno all'esterno dell'edificio - potrebbe non esserci - e' un elenco
		self.portals = []
		# elenco di relazioni di gruppo - la chiave e' l'id dellla relazione
		self.groups = dict()

