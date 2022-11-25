import json
import yaml
import os

#
# with open('dapao.json') as file:
#     w = json.load(file)
#     file.close()

with open('123.yaml', encoding="utf-8") as f2:
    w = yaml.load(f2, Loader=yaml.FullLoader)
    f2.close()

print(w)
print(type(w))
print(f2)
print(type(f2))


def generate_yaml_doc_ruamel(yaml_file):
    from ruamel import yaml

    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(w, file, Dumper=yaml.RoundTripDumper)
    file.close()


current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "generate.yaml")
generate_yaml_doc_ruamel(yaml_path)
