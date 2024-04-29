from collections import deque

def max_billboard(building_h):
    temp = 0
    height = []
    width = []
    max = 0
    for val in building_h:
        if len(height) != 0:
            if height[-1] < val:
                height.append(val)
                width.append(1)
            else:
                temp = 0
                while(len(height) != 0 and height[-1] >= val):
                    s = height[-1] * (width[-1] + temp)
                    temp = temp + width[-1]
                    if s > max: max = s
                    height.pop()
                    width.pop()
                height.append(val)
                width.append(temp + 1)
        else:
            height.append(val)
            width.append(1)

    temp = 0
    while(len(height) != 0):
        s = height[-1] * (width[-1] + temp)
        temp = temp + width[-1]
        if s > max: max = s
        height.pop()
        width.pop()
    return max


n = int(input())
building_h = [int(chr) for chr in input().split()]

print(max_billboard(building_h))
