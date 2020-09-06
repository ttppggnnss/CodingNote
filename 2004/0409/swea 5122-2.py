import sys
sys.stdin=open('../input.txt','r')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummy = Node('dummy')
        self.length = 0

    def insert(self, idx, data):
        cur = self.dummy
        for i in range(idx):
            cur = cur.next
        new = Node(data)
        new.next = cur.next
        cur.next = new
        self.length += 1

    def delete(self, idx):
        cur = self.dummy
        for i in range(idx):
            cur = cur.next
        cur.next = cur.next.next
        self.length -= 1

    def change(self, idx, datum):
        cur = self.dummy
        for i in range(idx+1):
            cur = cur.next
        cur.data = datum

    def get(self, idx):
        if idx + 1 > self.length:
            return -1
        else:
            cur = self.dummy
            for i in range(idx+1):
                cur = cur.next
            return cur.data

for tc in range(1, int(input())+1):
    N, M, L = map(int,input().split())
    LL = LinkedList()
    data = list(map(int,input().split()))

    for idx, data in enumerate(data):
        LL.insert(idx, data)

    for i in range(M):
        command = list(input().split())
        if command[0] == 'I':
            LL.insert(int(command[1]), int(command[2]))
        elif command[0] == 'D':
            LL.delete(int(command[1]))
        else:
            LL.change(int(command[1]), int(command[2]))

    print("#%d"%tc, LL.get(L))