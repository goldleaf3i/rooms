''' test di utils.py - dict_to_xmlDOC
import utils
import xml.dom.minidom
a = {"a": 12, "b" : {"C":4,"D":'asda'}}
doc = xml.dom.minidom.Document()
c = doc.createElement('test')
utils.dict_to_xml(a,doc,c)
doc.appendChild(c)
 fine test '''
import utils
import xml.etree.ElementTree as ET
a = {"a": 12, "b" : {"C":4,"D":'asda'}}
'''
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)
<a><b /><c><d /></c></a>
'''
doc = ET.Element('test')
utils.dict_to_xml(a,doc)
ET.dump(doc)
tree = ET.ElementTree(doc)
tree.write('test.xml')
tree = ET.parse('test.xml')
root = tree.getroot()
a = root.find('a')
print a.text , " e' il testo di a"