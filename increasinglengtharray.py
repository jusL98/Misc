num = 10
array = []
temp = []
symbol = ">"

# Forward
for i in range(0,num+1,1):
    for j in range(i):
        temp.append(symbol)
    array.append(temp)
    temp = []

for list in array:
    print("".join(list))

# Reset
array = []
print()

# Reverse
for i in range(num,0,-1):
    for j in range(i):
        temp.append(symbol)
    array.append(temp)
    temp = []

for list in array:
    print("".join(list))