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
            result_lines.append("'" + hifen_class_name + "': reverse('bcim:" + class_name + "_list', args=args, kwargs=kwargs, request=request),\n")
            continue

with open('temp.py', 'w') as views_file:
    for line in result_lines:
        views_file.writelines(line)