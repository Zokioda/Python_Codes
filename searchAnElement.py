i = int(input("Enter the size of list :"))
j = 0
l1 = []
while j < i:
    l1.append(int(input()))
    j += 1
n = int(input("Find : "))
j = 0
found = False
while j < i:
    if n == l1[j]:
        print(n, " found at index ", j)
        found = True
        break
    j += 1
if not found:
    print(n, " not found")
