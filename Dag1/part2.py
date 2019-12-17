total = 0
for i in open("c:/Users/raasvest/dev/adventOfCode/Dag1/data.txt","r"):
    totalModuleFuel = (int(i)//3)-2
    moduleFuel = totalModuleFuel
    while (moduleFuel > 0):
        totalModuleFuel += (moduleFuel//3)-2 if ((moduleFuel//3)-2 > 0) else 0
        moduleFuel = (moduleFuel//3)-2
    total += totalModuleFuel
print(total)