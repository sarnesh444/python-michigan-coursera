#for parsing xml doc
import xml.etree.ElementTree as ET
data='''
<person>
<users>
<user>
<name>Chuck</name>
<email hide="yes"/>
</user>
<user>
<name>Chik</name>
<email hide="no"/>
</user>
</users>
</person>
'''
#constructs xml tree from the str
#if this line does not work there is an XML issue
tree=ET.fromstring(data)
lst=tree.findall('users/user')
for l in lst:
    print("Name :",l.find("name").text)
    print("Email :",l.find("email").get('hide'))
