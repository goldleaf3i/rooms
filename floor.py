# intestazione

# fine intestazione

class floor(object) :

	def __init__(self, filename, extension = 'xml', myformat = None, building_type = None) :
		"""
		""" 
		# building_type è il nome del file da cui devo prendere l'xml oppure già l'xml

		# spaces e' quello piu importante - gestisce le stanze
		self.spaces = dict()
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
		self.contour = []
		# lista di linesegments del contonro - potrebbe non esserci - e' un elenco
		self.linesegments = []
		# lista di porte che danno all'esterno dell'edificio - potrebbe non esserci - e' un elenco
		self.portals = []
		# elenco di relazioni di gruppo - la chiave e' l'id dellla relazione
		self.groups = dict()

		if extension == 'xml' :
			load_from_xml(filename,myformat, building_type)
		elif :
			#TODO
			pass

	def load_from_xml(self,filename,myformat,building_type) :
		if myformat = "STANDARD" :
			xml_name = filename
			print xml_name
			tree = ET.parse(xml_file)
			root = tree.getroot()
			floor = root.find('floor')
			spacesxml = floor.find('spaces')
			pixels = int(root.find('scale').find('represented_distance').find('value').text)

			# parso stanza per stanza
			for s in spacesxml.iter('space'):

				# parso le informazioni primarie su di una stanza
				space_id = s.get('id')
				pointsxml = []
				area = 0
				perimeter = 0
				DCS = []
				label = s.find('labels')
				TODO 

				# parso il controno della stanza
				for point in s.find('bounding_polygon').findall('point'):
					pointsxml += [(int(point.get('x'))/pixels,int(point.get('y'))/pixels)]
				centxml = s.find('centroid').find('point')
				cent = (int(centxml.get('x'))/pixels,int(centxml.get('y'))/pixels)

				'''
			   	<bounding_box>
			          <maxx>
			            <point x="324" y="606"/>
			          </maxx>
			          <maxy>
			            <point x="299" y="644"/>
			          </maxy>
			          <minx>
			            <point x="299" y="644"/>
			          </minx>
			          <minY>
			            <point x="299" y="644"/>
			          </minY>
			        </bounding_box>
			    '''

			    # inizio a parsare la space_representation
				space_representation = dict()

				linesxml = dict()
				for line in s.find('space_representation').findall('linesegment'):
					'''
					   <linesegment id="3534b030-9151-4e55-a77c-50ce705f8873">
			            <point x="124" y="584"/>
			            <point x="124" y="637"/>
			            <class>WALL</class>
			            <type>EXPLICIT</type>
			            <features>NORMAL</features>
			          </linesegment>
			        '''
			        line_id = line.get('id')
			        linepointsxml = []
			        for point in s.findall('point'):
						linepointsxml += [(int(point.get('x'))/pixels,int(point.get('y'))/pixels)]
					classxml = p.find("class")
					l_class = classxml.text
					typexml = p.find("type")
					l_type = typexml.text
					featuresxml = p.find("features")
					l_features = featuresxml.text
					#
					space_representation[line_id] = linesegment( linepointsxml, mytype = l_type, myclass = l_class, features = l_features, uid = line_id)


				# parso le porte della stanza
				for p in s.find('portals').find('portal'):			
					'''
					<portal>
			            <linesegment>3d8c554d-80a9-4f5a-9148-9766d57d860f</linesegment>
			            <class>HORIZONTAL</class>
			            <type>EXPLICIT</type>
			            <features>NORMAL</features>
			            <direction>BOTH</direction>
			            <target>
			              <id>4fd5fb65-3187-4528-95cb-e465c5b42a02</id>
			              <id>e819bec5-28f7-4197-b49d-0da26f12688a</id>
			            </target>
			          </portal>
					'''
					ls = p.find("linesegment")
					p_id = ls.text
					classxml = p.find("class")
					p_class = classxml.text
					typexml = p.find("type")
					p_type = typexml.text
					featuresxml = p.find("features")
					p_features = featuresxml.text
					directionxml = p.find("direction")
					p_direction = directionxml.text
					p_ids =[]
					for idx in p.findall('id'):
						p_ids += [idx.text]


				space_object = space(label, space_representation = space_representation, bounding_polygon = pointsxml, portals = None, boundingbox = pointsxml, centroid = cent ) )
				self.spaces[space_id] = space_object 

				#area = find_area (points)
				#perimeter = find_perimeter (points)
				#DCS = dist_centr_bound(cent,points)

