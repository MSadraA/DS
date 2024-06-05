import heapq
import sys

X = 0
Y = 1

X_MIN = 0
Y_MIN = 1

X_MAX = 0
Y_MAX = 1


MAX = 10 ** 9
MIN = 0

EMPTY = ()

class COORDINATE:

    def __init__(self):
        self.coordinates = []
        self.size = 0

        self.max_x_point = [MIN]
        self.min_x_point = [MAX]

        self.max_y_point = [MIN]
        self.min_y_point = [MAX]

        self.point_1 = EMPTY
        self.point_2 = EMPTY
        self.point_3 = EMPTY
        self.point_4 = EMPTY

        self.point_1_neighbor = EMPTY
        self.point_2_neighbor = EMPTY
        self.point_3_neighbor = EMPTY
        self.point_4_neighbor = EMPTY

    def insert(self , pare):
        self.coordinates.append(pare)
        self.size += 1
        #find limits
        falg = False

        # if(len(self.coordinates) == 1):
        #     self.min_x_point.append(pare[X])
        #     self.min_x_point.append(pare[Y])
        #     self.min_x_point.append(pare[Y])
        #     self.max_y_point.append[pare[Y]]
    
        if(pare[X] <= self.min_x_point[-1]):
            self.min_x_point.append(pare[X])
            falg = True

        if(pare[Y] <= self.min_y_point[-1]):
            self.min_y_point.append(pare[Y])
            falg = True
        
        if(pare[X] >= self.min_x_point[-1]):
            self.max_x_point.append(pare[X])
            falg = True
        
        if(pare[Y] >= self.max_y_point[-1]):
            self.max_y_point.append(pare[Y])
            falg = True

        if(falg):
            self.fill_points()
            self.point_1_neighbor = self.find_point_neighbor(self.point_1)
            self.point_2_neighbor = self.find_point_neighbor(self.point_2)
            self.point_3_neighbor = self.find_point_neighbor(self.point_3)
            self.point_4_neighbor = self.find_point_neighbor(self.point_4)

        # self.print_all()
        # self.print_points()


    def fill_points(self):
        self.point_1 = (self.max_x_point[-1] , self.max_y_point[-1])
        self.point_2 = (self.min_x_point[-1] , self.max_y_point[-1])
        self.point_3 = (self.min_x_point[-1] , self.min_y_point[-1])
        self.point_4 = (self.max_x_point[-1] , self.min_y_point[-1])

    def find_point_neighbor(self , point):
        min = 2 * MAX
        near_point = point
        
        for p in self.coordinates:
            if(p != EMPTY):
                dist = abs(p[X] - point[X]) + abs(p[Y] - point[Y])
                if(dist < min):
                    min = dist
                    near_point = p
        return near_point
        
    def print_points(self):
        print("point_1 :" + str(self.point_1))
        print("point_2 :" + str(self.point_2))
        print("point_3 :" + str(self.point_3))
        print("point_4 :" + str(self.point_4))
        print("point_1_eighbor :" + str(self.point_1_neighbor))
        print("point_2_eighbor :" + str(self.point_2_neighbor))
        print("point_3_eighbor :" + str(self.point_3_neighbor))
        print("point_4_eighbor :" + str(self.point_4_neighbor))
    
    def delete(self , index):
        i = index - 1
        flag = False
        if(i >= 0 and i < len(self.coordinates) and self.coordinates[i] != EMPTY):
            if(self.coordinates[i][X] == self.max_x_point[-1]):
                self.max_x_point.pop()
                flag = True
            if(self.coordinates[i][X] == self.min_x_point[-1]):
                self.min_x_point.pop()
                flag = True
            if(self.coordinates[i][Y] == self.max_y_point[-1]):
                self.max_y_point.pop()
                flag = True
            if(self.coordinates[i][Y] == self.min_y_point[-1]):
                self.min_y_point.pop()
                flag = True

            if(flag):
                self.fill_points()
                self.point_1_neighbor = self.find_point_neighbor(self.point_1)
                self.point_2_neighbor = self.find_point_neighbor(self.point_2)
                self.point_3_neighbor = self.find_point_neighbor(self.point_3)
                self.point_4_neighbor = self.find_point_neighbor(self.point_4)

            self.coordinates[i] = EMPTY
            self.size -= 1

        # self.print_all()
        # self.print_points()
           
    def find_max_distance(self , pare):
        #find region
        x_edge = abs(self.max_x_point[-1] - self.min_x_point[-1]) / 2 + self.min_x_point[-1]
        y_edge = abs(self.max_y_point[-1] - self.min_y_point[-1]) / 2 + self.min_y_point[-1]
        
        target_point = pare
        if(x_edge <= pare[X]):
            if(y_edge <= pare[Y]):#region 1
                target_point = self.point_3_neighbor
            else:#region 4
                target_point = self.point_2_neighbor
        elif(x_edge > pare[X]):
            if(y_edge <= pare[Y]):#region 2
                target_point = self.point_4_neighbor
            else:#region 3
                target_point = self.point_1_neighbor

    
        return abs(pare[X] - target_point[X]) + abs(pare[Y] - target_point[Y])

    
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
