total = 0
for i in open("c:/Users/raasvest/dev/adventOfCode/Dag1/data.txt","r"):
    total += (int(i)//3)-2
print(total)