import sys

X = 0
Y = 1

EMPTY = ()

class COORDINATE:

    def __init__(self):
        self.coordinates = []
       

    def insert(self , pare):
        self.coordinates.append(pare)
    
    def delete(self , index):
        i = index - 1
        if(i >= 0 and i < len(self.coordinates) and self.coordinates[i] != EMPTY):
            self.coordinates[i] = EMPTY
           
    def find_max_distance(self , pare):
        max = 0
        for p in self.coordinates:
            if(p != EMPTY):
                temp = abs(p[X] - pare[X]) + abs(p[Y] - pare[Y])
                if(temp > max):
                    max = temp
        return max
    
    def print_all(self):
        print(self.coordinates)

def main():
    n = int(input())

    a = [list(input().split()) for _ in range(n)]
    c = COORDINATE()
    
    for x in a:
        if(x[0] == '+'):
            c.insert((int(x[1]) , int(x[2])))
        if(x[0] == '-'):
            c.delete(int(x[1]))
        if(x[0] == '?'):
            print(c.find_max_distance((int(x[1]) , int(x[2]))))

        # c.print_all()
    
if __name__ == "__main__":
    main()
