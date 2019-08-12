class_name = None
result_lines = []
TAB1x = (4 * " ")
TAB2x = (8 * " ")

with open('models.py', 'r') as models_file:
    for line in models_file.readlines():
        if "class " in line and "(" in line and "#" not in line:
            field_list = []
            class_name = line[5:].split("(")[0].strip()
            result_lines.append("class " + class_name + "List(FeatureCollectionResource):\n")
            result_lines.append(TAB1x + "serializer_class = " + class_name + "Serializer\n\n")
            result_lines.append("class " + class_name + "Detail(FeatureResource):\n")
            result_lines.append(TAB1x + "serializer_class = " + class_name + "Serializer\n\n")
            continue

with open('views_temp.py', 'w') as views_file:
    for line in result_lines:
        views_file.writelines(line)