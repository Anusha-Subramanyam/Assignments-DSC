from collections import Counter
num = input("Enter total number of gloves : ")
print("Enter colors of array : ")
arr = list(map(int,input().split()))

sum = 0
n = Counter(arr)
for i in n.values():
    sum += (i//2)

print(sum)