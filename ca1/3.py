n = int(input())
numbers = [x+1 for x in range(n)]

def find_arrays(index , array , counter):  
    if(len(array)==0):
        counter[0] += 1

    for n in array:
        if (n % (index + 1) == 0 or (index + 1) % n == 0):
            array_ = [x for x in array if x!= n]
            find_arrays(index+1 , array_ , counter)

counter = [0]
index = 0
find_arrays(index, numbers , counter)
print(counter[0])