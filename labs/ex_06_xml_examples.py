import xml.etree.ElementTree as ET

root = ET.parse('canteen.xml') #ElementTree instance

datums = root.findall('date') #list of Elements

for date in dates:
    print(datum.attrib['day'])
    meals = datum.iter('meal')
    for meal in meals:
        print('\t' + meal.attrib['name'])
        for ingredience in meal.iter('ingredience'):
            print('\t\t' + ingredience.attrib['name'])


def xml2py(node):
    name = node.tag

    pytype = type(name, (object, ), {})
    pyobj = pytype()

    for attr in node.attrib.keys():
        setattr(pyobj, attr, node.get(attr))

    if node.text and node.text != '' and node.text != ' ' \
                 and node.text != '\n':
        setattr(pyobj, 'text', node.text)

    for cn in node:
        if not hasattr(pyobj, cn.tag):
            setattr(pyobj, cn.tag, [])
        getattr(pyobj, cn.tag).append(xml2py(cn))

    return pyobj

xml_string = ''
with open('canteen.xml', 'rt') as f:
    xml_string = f.read()

menza_xml_tree = ET.fromstring(xml_string)

obj = xml2py(menza_xml_tree)

for date in obj.date:
    print(datum.day)
    for meal in date.meal:
        print('\t' + meal.name)
        for ingredience in meal.ingredience:
            print('\t\t' + ingredience.name)
