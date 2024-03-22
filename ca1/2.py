import sys

init = list(input())
goal = list(input())

size = len(goal)

find = True

if(len(init) != size):
    print("no")
    sys.exit()
    
for i in range(size):
    if(find == False):
        break
    if(init[i] != goal[i]):
        for j in range(i , size , 2):
            if(init[j] == goal[i]):
                init[i] , init[j] = init[j] , init[i]
                break
            elif(j >= size -1):
                find = False
if(find):
    print("yes")
else:
    print("no")


    