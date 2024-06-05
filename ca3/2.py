LEFT = 1
RIGHT = 2
VALUE = 0
EMPTY = -2

class Bst:
    class Node:
        def __init__(self , value=None , parent=None , l_child=None , r_child=None):
            self.value = value
            self.parent = parent
            self.left = l_child
            self.right = r_child

    def __init__(self):
        self.values = []
        self.root = None
    
    def build_tree(self , l):
        nodes = [self.Node(value=l[i][VALUE] , l_child=l[i][LEFT]-1 , r_child=l[i][RIGHT]-1) for i in range(len(l))]
        for x in nodes:
            if(x.right != EMPTY):
                x.right = nodes[x.right]
                x.right.parent = x
            else:
                x.right = None

            if(x.left != EMPTY):
                x.left = nodes[x.left]
                x.left.parent = x
            else:
                x.left = None
            
            self.values.append(x.value)
        
        for x in nodes:
            if x.parent == None:
                self.root = x
                break

    def search(self , cur_node=None , key= None):
        if(cur_node == None):
            return False
        
        if(cur_node.value > key):
            if(self.search(cur_node.left , key)):
                return True
        if(cur_node.value < key):
           if(self.search(cur_node.right , key)):
               return True
        if(cur_node.value == key):
            return True
        else:
            return False
        
    def count_invalid_nodes(self):
        counter = 0
        for key in self.values:
            if(self.search(cur_node=self.root , key=key) == False):
                counter += 1
        return counter

def main():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    T = Bst()
    T.build_tree(a)
    print(T.count_invalid_nodes())

if __name__ == "__main__":
    main()
