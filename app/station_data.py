import xml.etree.ElementTree as ET

tree = ET.parse('./data/NLC20261002.xml')
root = tree.getroot()

print(root.tag)

ns = {
    'ns2' : 'http://tempuri.org/XMLSchema.xsd'
}

items = root.findall('ns2:TSDBDataItem', ns)

# print(type(items))
# print(len(items))
# print(type(items[0]))

# first_item = items[0]

# description = first_item.find("ns2:NLCDescription", ns)
# crs = first_item.find("ns2:NLCCrsCode", ns)

# print(description)
# print(description.text)

# print(crs)
# print(crs.text)

def get_station_code(station_name) :
    station_name = station_name.upper()
    for item in items:
        description = item.find("ns2:NLCDescription", ns)
        if description.text == station_name :
            crs = item.find("ns2:NLCCrsCode", ns)
            return crs.text

    return None

print(get_station_code("WoKiNg"))