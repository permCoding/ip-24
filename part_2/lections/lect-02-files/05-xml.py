import xml.etree.ElementTree as ET

 
tree = ET.parse('./data/customers.xml')
root = tree.getroot()

for elem in root.find('Customers').findall('Customer'):
    print(elem.tag, elem.attrib, elem.find('ContactName').text)
