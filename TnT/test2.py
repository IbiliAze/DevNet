# import xml.etree.ElementTree as et
from lxml import etree as et
import xmltodict
import xml.dom.minidom
from pprint import pprint as p



# stream = open("test.xml", "r")
# # print(type(stream))


# xml = et.parse(stream)
# root = xml.getroot()

# for sub_element in root:
#     print(et.tostring(sub_element))
#     print()




# dict1 = xmltodict.parse(stream.read())
# p(dict1)


# print(xml.dom.minidom.parse(stream).toprettyxml())
