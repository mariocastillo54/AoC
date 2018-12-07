import re 
inputdata = open("Day5.txt").read().split()
print(inputdata[0])

list = inputdata[0]

capitals = []
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(lowercase)):
    capitals.append( lowercase[i].capitalize())
print(capitals)

combinations = []
for n in range(len(lowercase)):
    combinations.append(str(lowercase[n]) + str(capitals[n]))
    combinations.append(str(capitals[n]) + str(lowercase[n]))

print(combinations)


lowerbound = 10762
x = 0
while x < 26:
    
    react = list
    react = re.sub(capitals[x],'', react)
    react = re.sub(lowercase[x],'', react)

    check = 0

    while check == 0:
        startlen = len(react)
        for combo in combinations:
                react = re.sub(combo,'',react)
        endlen = len(react)
        if startlen == endlen:
            check = 1
    x = x + 1

    if len(react) < lowerbound:
        lowerbound = len(react)

print(lowerbound)
