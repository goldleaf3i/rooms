#!
import xml.dom.minidom
import uuid

def dict_to_xml(dictionary, doc, elem):
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

	for i in dictionary.keys() :
		tmp = doc.createElement(str(i))
		content = doc.createTextNode(str(dictionary[i]))
		if type(dictionary[i]) is dict :
			dict_to_xml(dictionary[i],doc,tmp)
		else :
			tmp.appendChild(content)
		element.appendChild(tmp)



def getId(length = 6) :
	'''
	returns a uniqueID of size "length" characters
	'''
	return str(uuid.uuid4())[:length]