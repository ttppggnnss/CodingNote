import sys
sys.stdin=open('../input.txt','r')

class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.count=0

    def append(self,node):
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def get(self,idx):
        cur=self.head
        cur_i=0
        while cur_i<idx:
            cur=cur.next
            cur_i+=1
        return cur.data

    def insert(self, idx, node):
        cur=self.head
        pre=None
        cur_i=0
        if idx==0:
            if self.head:
                nxt=self.head
                self.head=node
                self.head.next=nxt
            else:
                self.head=node
        else:
            while cur_i<idx:
                if cur:
                    pre=cur
                    cur=cur.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                node.next=cur
                pre.next=node
            else:
                return -1

for tc in range(1,int(input())+1):
    n,m,l=map(int,input().split())
    L=LinkedList()
    data=list(map(int,input().split()))
    for i in range(n):
        L.append(Node(data[i]))
    for i in range(m):
        idx,d=map(int,input().split())
        L.insert(idx,Node(d))
    print('#%i'%tc,L.get(l))