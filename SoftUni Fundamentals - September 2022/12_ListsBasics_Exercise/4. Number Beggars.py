list = input().split(", ")
list1 = []
list2 = []
a = int(input())
for i in range(a):
    for j in range(i, len(list), a):
        list1.append(int(list[j]))
    list2.append(sum(list1))
    list1.clear()
print(list2)