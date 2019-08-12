field_list = []
class_name = None
geom_field_name = "geom"
id_field_name = "gid"
result_lines = []
TAB1x = (4 * " ")
TAB2x = (8 * " ")

with open('models.py', 'r') as models_file:
    result_lines.append("from rest_framework_gis.serializers import GeoFeatureModelSerializer\n")
    result_lines.append("from .models import *\n\n")
    for line in models_file.readlines():
        if "class " in line and "(" in line and "#" not in line:
            field_list = []
            class_name = line[5:].split("(")[0].strip()
            result_lines.append("class "+class_name+"Serializer(GeoFeatureModelSerializer):\n")
            continue

        elif ("=" in line) and ("#" not in line) and ("models." in line) and ("geom" not in line):
            field_list.append( line.split("=")[0].strip() )
            continue

        elif "class Meta:" in line and "#" not in line:
            #for field_name in field_list:
            result_lines.append(TAB1x + "class Meta:\n")
            result_lines.append(TAB2x + "model = " + class_name + "\n")
            result_lines.append(TAB2x + "geo_field = 'geom'\n")
            result_lines.append(TAB2x + "auto_bbox = True\n")
            result_lines.append(TAB2x + "id_field = 'gid'\n")
            result_lines.append(TAB2x + "fields = " + str(field_list) + '\n\n')
            continue

with open('serializer_temp.py', 'w') as serializers_file:
    for line in result_lines:
        serializers_file.writelines(line)