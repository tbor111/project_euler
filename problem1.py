list = range(1,1000)

new_list = []
for i in list:
    new_list.append(float(i))

mult = []

for i in new_list:
    if (i/5).is_integer() == True:
        mult.append(i)
    elif (i/3).is_integer() == True:
        mult.append(i)

print sum(mult)
