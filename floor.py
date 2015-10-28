# intestazione

# fine intestazione

class floor(object) :

	def __init__(self, filename, extension = 'xml', format = None, building_type = None) :
		"""
		"""

		# building_type è il nome del file da cui devo prendere l'xml oppure già l'xml
		spaces = []
		connections = []
		name = str()
		scale = ()
		# chiave : campo; valore: valore del campo (anche stringa o dict)
		info = dict()
		# chiave: campo; valore: ...
		building_type = dict()