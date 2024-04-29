from collections import deque


class Stack:
    def __init__(self, capacity=10):
        self.stack = ['_'] * capacity
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

def is_substring_valid(start_index , end_index , s):
    stack = Stack(end_index - start_index + 1)
    stack.push(s[start_index-1])
    for i in range(start_index , end_index):
        if s[i] == stack.peek().lower() and stack.peek() != s[i]:
            stack.pop()
        else:
            stack.push(s[i])
    if stack.empty():
        return "1"
    return "0"

def main():
    s = input()
    q = int(input())
    res = ""
    for _ in range(q):
        i , j = map(int, input().split())
        res += is_substring_valid(i , j , s)
    print(res)

if __name__ == "__main__":
    main()

    
