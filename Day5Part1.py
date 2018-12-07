import re 
inputdata = open("day5.txt").read().split()

print(inputdata[0])

list = inputdata[0]

capitals = []
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(lowercase)):

    capitals.append( lowercase[i].capitalize())
    print(capitals)

combination = []
for n in range(len(lowercase)):
    combination.append(str(lowercase[n]) + str(capitals[n]))
    combination.append(str(capitals[n]) + str(capitals[n]))

print(combination)

check = 0
react = list

while check == 0:
    startlen = len(react)
    for combo in combination:
            react = re.sub(combo,'',react)
    endlen = len(react)
    if startlen == endlen:
        check = 1
print(react)
print(len(react))
