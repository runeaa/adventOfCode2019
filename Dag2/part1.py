input = open("c:/Users/raasvest/dev/adventOfCode/Dag2/data.txt","r")

for i in input:
    print(i)
for x in range(0, len(input)-4, 4):
    if(input[x] == 99):
        break
    if(input[x] == 1):
        input[input[x+3]] = input[input[x+1]] + input[input[x+2]]
        continue    
    if(input[x] == 2):
        input[input[x+3]] = input[input[x+1]] * input[input[x+2]]
        continue
print(input)

input.close()