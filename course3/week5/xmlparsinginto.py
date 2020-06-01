#for parsing xml doc
import xml.etree.ElementTree as ET
data='''
<person>
<name>Chuck</name>
<email hide="yes"/>
</person>
'''
#constructs xml tree from the str
#if this line does not work there is an XML issue
tree=ET.fromstring(data)
print("Name :",tree.find('name').text)
print("Email :",tree.find('email').get('hide'))