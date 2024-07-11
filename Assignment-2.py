# find min and max item
ls = [23,65,12,86,16,2,7,65,77,3]
min = ls[0]
max = ls[0]
for i in ls :
    if i < min:
        min = i
    if i > max :
        max = i
print("min -> ", min, "max -> ", max)

# star pattern
n = int(input("Enter number of rows: "))
for i in range(0,n):
    for j in range (0, i+1):
        print("*",end="")
    print()

# number pattern
n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j,end="")
    print()