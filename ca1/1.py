s = input()

maxLength = 0

size = len(s) - 1
ispair = False
start_index = 0
j_index = 0

for i in range(size):
    j = i + 1
    if(s[i] == s[j]):
        if(ispair):
            start_index = j_index
            j_index = j
        else:
            j_index = j
            ispair = True

    if(j - start_index + 1> maxLength):
        maxLength = j - start_index + 1

print(maxLength)
