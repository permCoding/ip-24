lst = list()  # []
tpl = tuple()  # ()
st = set()  # {}
dct = dict()  # { "id": 123 }
dict(zip([], []))
# tree()
st.add(1)
lst.append(1)
lst.extend(lst)

# *.csv => *.json
s = 'id,name,rate,gender'
t = s.split(',')
d = [12, 'Коля', 23.5]
# for item in zip(t, d):
#     print(item)
studs = list(zip(t, d))
print(studs)

studs = dict(zip(t, d))
print(studs)

import json

str = json.dumps(studs, indent=4, ensure_ascii=False)

print(str)