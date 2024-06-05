import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        pass

    def ckeck_for_exeption(self , index):
        if type(index) != int:
            raise Exception (INVALID_INDEX)
        if (index >= self.size or index < 0):
            raise Exception (OUT_OF_RANGE_INDEX)
        if self.size == 0:
            raise Exception (EMPTY)

    def bubble_up(self, index):
        self.ckeck_for_exeption(index)

        parent_pos = int((index - 1) / 2)
        value = self.heap[index]
        while(index > 0):
            if(value < self.heap[parent_pos]):
                self.heap[parent_pos] , self.heap[index] = self.heap[index] , self.heap[parent_pos]
            else : break
            index = parent_pos
            parent_pos = int((parent_pos - 1) / 2)
        
        self.heap[index] = value

    def bubble_down(self, index):
        self.ckeck_for_exeption(index)
        
        L_child_pos = index * 2 + 1
        R_child_pos = index * 2 + 2
        min_pos = index

        if (L_child_pos < self.size and self.heap[L_child_pos] < self.heap[min_pos]):
            min_pos = L_child_pos
        if(R_child_pos < self.size and self.heap[R_child_pos] < self.heap[min_pos]):
            min_pos = R_child_pos
        if(min_pos != index):
            self.heap[min_pos] , self.heap[index] =  self.heap[index] , self.heap[min_pos]
            self.bubble_down(min_pos)

    def heap_push(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size - 1)

    def heap_pop(self):
        if(self.size == 0):
            raise Exception(EMPTY)
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.size -= 1
        if(self.size != 0):
            self.bubble_down(0)
        return value

    def find_min_child(self, index):
        self.ckeck_for_exeption(index)

        L_child_pos = index * 2 + 1
        R_child_pos = index * 2 + 2
        min_pos = index

        if(L_child_pos < self.size):
            min_pos = L_child_pos
        if(R_child_pos < self.size):
            if(self.heap[R_child_pos] < self.heap[min_pos]):
                min_pos = R_child_pos
        return min_pos
        

    def heapify(self, *args):
        for x in args:
            self.heap_push(x)


class HuffmanTree:
    class Node:
        def __init__(self , letter = None , frequency = None , parent = None , l_child = None , r_child = None):
            self.letter = letter
            self.frequency = frequency
            self.left = l_child
            self.right = r_child
            self.parent = parent
        pass

    def __init__(self):
        self.letters = []
        self.freqs = []
        self.root = self.Node()
        pass

    def set_letters(self, *args):
        for letter in args:
            self.letters.append(letter)

    def set_repetitions(self, *args): 
        for freq in args:
            self.freqs.append(freq)
        

    def build_huffman_tree(self):
        sorted_letters = [x for _ , x in sorted(zip(self.freqs , self.letters) , reverse=True)]
        sorted_freqs = sorted(self.freqs , reverse=True)
        # make nodes by sorted_letters
        nodes = []
        for i in range(len(self.letters)):
            nodes.append(self.Node(letter=sorted_letters[i] , frequency=sorted_freqs[i]))

        while(len(nodes) > 1):
            r = nodes.pop()
            l = nodes.pop()
            p = self.Node(frequency= (r.frequency + l.frequency))
            p.left = l
            p.right = r
            r.parrent = p
            l.parrent = p
            nodes.append(p)
            nodes.sort(key=lambda node: node.frequency , reverse=True)
            self.root = nodes[0]

    def print_tree(self , t):
        if(t == None):
            return
        print((t.letter , t.frequency))
        self.print_tree(t.left)
        self.print_tree(t.right)

    def calculation_cost(self , cur_node : Node , length , cost):
        if(cur_node == None):
            return

        if(cur_node.left == None and cur_node.right == None):
            cost[0] += cur_node.frequency * length
        
        self.calculation_cost(cur_node.left , length +1 , cost)
        self.calculation_cost(cur_node.right , length +1 , cost)

    def get_huffman_code_cost(self):
        length = 0
        cost = [0]
        cur_node = self.root

        self.calculation_cost(cur_node=cur_node , length=length , cost=cost)
        return cost[0]
    
    def text_encoding(self, text):
        all_letters = {}
        for letter in text:
            if letter in all_letters:
                all_letters[letter] += 1
            else:
                all_letters[letter] = 1

        self.letters = list(all_letters.keys())
        self.freqs = list(all_letters.values())
        self.build_huffman_tree()


class Bst:
    class Node:
        def __init__(self , value=None , parent=None , l_child=None , r_child=None):
            self.value = value
            self.parent = parent
            self.left = l_child
            self.right = r_child

    def __init__(self):
        self.root = None

    def find_insert_pos(self , side=None , prev_node=None , cur_node=None , key=None):
        if(cur_node == None):
            new_node = self.Node(key)
            new_node.parent = prev_node
            if(side == "Left"):
                prev_node.left = new_node
            elif(side == "Right"):
                prev_node.right = new_node
            return

        if(key <= cur_node.value):
            self.find_insert_pos("Left" , cur_node , cur_node.left , key)
        else:
            self.find_insert_pos("Right" , cur_node , cur_node.right , key)

    def insert(self, key):
        if(self.root == None):
            self.root = self.Node(value=key)
            return
        self.find_insert_pos(cur_node=self.root , key=key)

    def make_inorder_list(self , node = None , inorder_list = None):
        if(node == None):
            return
        self.make_inorder_list(node.left , inorder_list)
        inorder_list.append(node.value)
        self.make_inorder_list(node.right , inorder_list)

    def inorder(self):
        l = []
        result = ""
        self.make_inorder_list(self.root , l)
        for node in l:
            result += (str(node) + ' ')
        return result
        


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
