from itertools import groupby

words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'cranberry']

words.sort()

gr_by = groupby(words, key=lambda x: x[0])

# for group in gr_by:
#     key, gro = group
#     print(key, list(gro))

# for key, group in gr_by:
#     print(key, list(group))

# lst = [[key, list(group)] for key, group in gr_by]
# print(lst)

grouped_lst = {key: list(group) for key, group in gr_by}
# print(grouped_lst)

import json
s_json = json.dumps(grouped_lst, indent=4, ensure_ascii=False)
print(s_json)
