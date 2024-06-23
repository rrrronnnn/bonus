d = {"a": 1, "b": 2, "c": 3}
reversed_dict = {}
for key, value in d.items():
	print(key)
	print(value)
	reversed_dict[value] = key
print(reversed_dict)