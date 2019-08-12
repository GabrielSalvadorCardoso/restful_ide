import re
class_name = None
result_lines = []
TAB1x = (4 * " ")
TAB2x = (8 * " ")
def camel_case_to_hifen(class_name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', class_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

def hifen_to_snake_case(class_name):
    class_name.replace("-", '_')
    return class_name

with open('models.py', 'r') as models_file:
    for line in models_file.readlines():
        if "class " in line and "(" in line and "#" not in line:
            class_name = line[5:].split("(")[0].strip()
            hifen_class_name = camel_case_to_hifen(class_name)
            snake_case_class_name = hifen_to_snake_case(class_name)

            result_lines.append("path('" + hifen_class_name + "/<int:pk>', " + class_name + "Detail.as_view(), name='" + snake_case_class_name + "_detail'),\n")
            result_lines.append("path('" + hifen_class_name + "', " + class_name + "List.as_view(), name='" + snake_case_class_name + "_list'),\n\n")
            continue

with open('views_temp.py', 'w') as views_file:
    for line in result_lines:
        views_file.writelines(line)