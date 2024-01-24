import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        return self.queue.popleft() if self.queue else -1
    
    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if not self.queue else 0
    
    def front(self):
        return self.queue[0] if self.queue else -1

    def back(self):
        return self.queue[-1] if self.queue else -1
    

if __name__ == '__main__':
    queue = Queue()
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'push':
            queue.push(cmd[1])
        elif cmd[0] == 'pop':
            print(queue.pop())
        elif cmd[0] == 'size':
            print(queue.size())
        elif cmd[0] == 'empty':
            print(queue.empty())
        elif cmd[0] == 'front':
            print(queue.front())
        elif cmd[0] == 'back':
            print(queue.back())