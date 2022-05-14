i = int(input("Enter the size of list :"))
j = 0
l1 = []
while j < i:
    l1.append(int(input()))
    j += 1

j = 0
while j < i:
    if l1[j] < 0:
        l1.remove(l1[j])
        l1.insert(j, 0)
    j += 1
print(l1)
