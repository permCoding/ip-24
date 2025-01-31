a = {}
lst = [
    ("id", 8),
    ("name", "Петров")
]
b = dict(lst)  # list() tuple()

a["id"] = 12
a["name"] = "Федоров"

print(a, b)
