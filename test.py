''' test di utils.py - dict_to_xml'''
import utils
import xml.dom.minidom
a = {"a": 12, "b" : {"C":4,"D":'asda'}}
doc = xml.dom.minidom.Document()
c = doc.createElement('test')
utils.dict_to_xml(a,doc,c)
doc.appendChild(c)
''' fine test '''