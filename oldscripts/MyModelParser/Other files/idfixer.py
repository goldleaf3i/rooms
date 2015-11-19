import xml.etree.ElementTree as ET
treea = ET.parse('a.xml')
treeb = ET.parse('b.xml')
roota = treea.getroot()
rootb = treeb.getroot()
floor = roota.find('floor')
spaces = floor.find('spaces')
nodes = rootb.find('nodes')
for space in spaces.iter('space'):
	centxml = space.find('centroid').find('point')
	cent = [int(centxml.get('x')),int(centxml.get('y'))]
	for node in nodes.iter('node'):
		posxml = node.find('position')
		pos = [int(posxml.get('x')),int(posxml.get('y'))]
		if pos==cent:
			ET.SubElement(node,'extid').set('value', space.get('id'))
			space.set('extid',node.find('id').text)



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

tree = treeb
root = tree.getroot()
indent(root)
tree.write('bplus.xml')

tree = treea
root = tree.getroot()
indent(root)
tree.write('aplus.xml')
