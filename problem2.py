L = [1, 2]
i = 1
condition = True

while condition == True:
    i = i + 1
    x = L[i - 1] + L[i-2]
    if x < 4000000:
        L.append(x)
    else:
        condition = False

new_L = []
for i in L:
    new_L.append(float(i))

even_L = []
for i in new_L:
    if (i/2).is_integer() == True:
        even_L.append(i)

print sum(even_L)
