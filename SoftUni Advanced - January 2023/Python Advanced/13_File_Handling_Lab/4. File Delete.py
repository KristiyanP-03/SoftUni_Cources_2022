dic_a = {'a': 0}
string = input()
for key in dic_a.keys():
    dic_a[key] = string.count(key)
print(dic_a)