#!
import xml.dom.minidom

def dict_to_xml(dictionary, xmlfile):
	'''
	receives a dictionary as {"a": 12, "b" : {"C":4,"D":'asda'}} and prints
	<a>
		12
	</a>
	<b>
		<c>4</c>
		<D>asda</D>
	</b>
	'''