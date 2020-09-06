import sys
sys.stdin=open('input.txt','r')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, *args):
        self.head = Node(args[0])
        self.count = 1
        temphead = self.head
        for i in range(1, len(args)):
            node = Node(args[i])
            temphead.next = node
            temphead = node
            self.count = self.count + 1
    def get(self, idx):
        tempidx = idx
        temphead = self.head
        while tempidx > 0:
            temphead = temphead.next
            tempidx -= 1
        return temphead
    def length(self):
        return self.count
    def add(self, idx, llst):
        if idx == 0:
            llst.get(llst.length() - 1).next = self.head
            self.head = llst.get(0)
        else:
            temphead = self.get(idx - 1)
            nextnode = temphead.next
            temphead.next = llst.head
            llst.get(llst.length() - 1).next = nextnode
        self.count = self.count + llst.count
    def list(self):
        result=[]
        temphead=self.head
        while temphead:
            result.append(temphead)
            temphead=temphead.next
        return result
    def __repr__(self):
        result = []
        temphead = self.head
        while temphead:
            result.append(str(temphead))
            temphead = temphead.next
        return ' '.join(result)

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    lst=LinkedList(*map(int,input().split()))
    for i in range(1,M):
        inp = LinkedList(*map(int,input().split()))
        for j in range(lst.length()):
            if lst.get(j).data>inp.get(0).data:
                lst.add(j, inp)
                break
        else:
            lst.add(lst.length(), inp)
    a=lst.list()
    print('#%i'%t,*a[::-1][:10])