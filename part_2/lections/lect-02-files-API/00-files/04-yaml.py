import yaml  # pip install pyyaml
import json


f = open('./data/103.yml')
data = yaml.safe_load(f)
f.close()

# print(data)

print(json.dumps(data, ensure_ascii=False, indent=2))

# for key in data.keys():
#     print(key, ':', data[key])