# Bubble sort - ASC order

list1 = [-2, 4, 5, 0, -1, 23, -32, 75, 26]
temp = 0
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)
