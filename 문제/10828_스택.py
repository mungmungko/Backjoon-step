import sys

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop() if self.stack else -1
    
    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0
    
    def top(self):
        return self.stack[-1] if self.stack else -1
    

if __name__ == '__main__':
    stack = Stack()
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'push':
            stack.push(cmd[1])
        elif cmd[0] == 'pop':
            print(stack.pop())
        elif cmd[0] == 'size':
            print(stack.size())
        elif cmd[0] == 'empty':
            print(stack.empty())
        elif cmd[0] == 'top':
            print(stack.top())