from xml.etree import ElementTree as ET

class XmlHandler:
    def __init__(self, xml_data):
        self.tree = ET.ElementTree(ET.fromstring(xml_data.strip()))
        self.root = self.tree.getroot()

    def xml_to_string(self):
        return ET.tostring(self.root, encoding='unicode')

    def from_str_to_xml(self, xml_string):
        self.root = ET.fromstring(xml_string.strip())
        self.tree = ET.ElementTree(self.root)

    def add_custom_tag(self, tag_name, attributes=None, text=None):
        new_element = ET.Element(tag_name, attributes if attributes else {})
        new_element.text = text
        self.root.append(new_element)

    def remove_custom_tag(self, tag_name):
        for element in self.root.findall(tag_name):
            self.root.remove(element)

    def get_elements_with_attributes(self, tag_name):
        return [(elem, elem.attrib) for elem in self.root.findall(tag_name)]

    def get_text_of_first_element_by_tag(self, tag_name):
        element = self.root.find(tag_name)
        if element is not None:
            return element.text
        else:
            return None


with open('example.xml', 'r', encoding='utf-8') as xml_file:
    xml_content = xml_file.read()


xml_handler = XmlHandler(xml_content)


xml_as_string = xml_handler.xml_to_string()
with open('xml_as_string.txt', 'w', encoding='utf-8') as file:
    file.write(xml_as_string)
print("XML to String:", xml_as_string)


xml_handler.remove_custom_tag('customTag')
print(xml_handler.xml_to_string())


elements_with_attributes = xml_handler.get_elements_with_attributes('food')
for elem, attrs in elements_with_attributes:
    print(f"Element: {elem.tag}, Attributes: {attrs}")


food_name = xml_handler.get_text_of_first_element_by_tag('food/name')
print(food_name)
