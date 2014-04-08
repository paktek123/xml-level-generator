import sys
import xml.etree.ElementTree as ET
import numpy

xml_file = sys.argv[1]

tree = ET.parse(xml_file)
root = tree.getroot()

level_width = root.attrib["width"]
level_height = root.attrib["height"]

level_content = [child.attrib for child in root]

matrix = [[" " for x in range(102)] for x in range(20)]

for x in matrix:
    x[0] = "|"
    x[-1] = "|"

matrix[0] = ["-" for x in matrix[0]]
matrix[-1] = ["-" for x in matrix[-1]]

factor_x = int(level_width) / 100
factor_y = int(level_height) / 20

for content in level_content:
    x, y, content_type = int(content["x"]), int(content["y"]), content["type"]
    scale_x = x / factor_x
    scale_y = y / factor_y

    if content_type == "platform1":
        rep = "_"
    elif content_type == "platform2":
        rep = "_"
    elif content_type == "platform3":
        rep = "_"
    elif content_type == "coin":
        rep = "O"
    elif content_type == "levelComplete":
        rep = "E"
    elif content_type == "player":
        rep = "P"

    matrix[-scale_y][scale_x] = rep

matrix_list = numpy.matrix(matrix).tolist()

for x in matrix_list:
    print ''.join(map(str,x))

