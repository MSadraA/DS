import sys
import re


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)

    def empty(self):
        return (len(self.queue) == 0)

    def one_line_str(self):
        s = ' '.join(self.queue)
        return s


class Stack:
    def __init__(self, capacity=10):
        self.stack = [0] * capacity
        self.top = -1
        

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        s = self.stack[self.top]
        if(self.top != -1):
            self.top -= 1
        return s

    def put(self, value):
        self.stack[self.top] = value

    def peek(self):
        return self.stack[self.top]

    def expand(self):
        self.stack *= 2

    def capacity(self):
        return len(self.stack)

    def size(self):
        return self.top + 1

    def empty(self):
        return self.top == -1

    def one_line_str(self):
        s = ""
        for i in range(self.top + 1):
            s += str(self.stack[i]) + ' '
        return s


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        cur_node = self.head
        next_node = self.head
        new_node = Node(value)

        if(self.head == None):
            self.head = new_node
            return

        while next_node != None:
            cur_node = next_node
            next_node = next_node.next

        cur_node.next = new_node

    def reverse(self):
        cur_node = None
        next_node = self.head

        while next_node != None:
            next = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = next

        self.head = cur_node

    def one_line_str(self):
        cur_node = self.head
        s = ""
        while cur_node != None:
            s += str(cur_node.value) + ' '
            cur_node = cur_node.next
        return s

class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
