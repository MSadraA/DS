from collections import deque


def call_commnds(command , list):
    commands = command.split()
    
    if commands[0] == "push_front":
        list.appendleft(int(commands[1]))
    elif commands[0] == "push_back":
        list.append(int(commands[1]))
    elif commands[0] == "reverse":
        list.reverse()
    elif commands[0] == "front":
        if len(list) == 0:
            print("No job")
        else:
            print(list.popleft())
    elif commands[0] == "back":
        if len(list) == 0:
            print("No job")
        else:
            print(list.pop())

def main():
    l = deque()
    q = int(input())
    for _ in range(q):
        command = input()
        call_commnds(command , l)

if __name__ == "__main__":
    main()
