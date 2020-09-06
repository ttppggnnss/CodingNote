# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

# Singly linked list 클래스 선언
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # Add new node at the end of the linked list
    def append(self, node):
        if self.head==None:
            self.head=node
        else:
            cur = self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    # return first index of data in the linked list
    def getdataIndex(self, data):
        cur=self.head
        idx=0
        while cur:
            if cur.data==data:
                return idx
            cur=cur.next
            idx+=1
        return -1

    # Add new node at the given index
    def insertNodeAtIndex(self,idx, node):
        """
        A node can be added in three ways
        1) At the front of the linked list
        2) At a given index
        3) At the end of the linked list
        """
        cur=self.head
        pre=None
        cur_i=0
        # (1) Add 0 index
        if idx==0:
            if self.head:
                nextn=self.head
                self.head=node
                self.head.next=nextn
            else:
                self.head=node
        else:
            # (2) Add at given index &
            # (3) At the end of the linked list
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

    # Add new node before the given data
    def insertNodeAtData(self,data,node):
        idx=self.getdataIndex(data)
        if 0<=idx:
            self.insertNodeAtIndex(idx,node)
        else:
            return -1

    # Delete data at given index
    def deleteAtIndex(self, idx):
        cur_i=0
        cur=self.head
        pre=None
        nextn=self.head.next
        if idx==0:
            self.head=nextn
        else:
            while cur_i<idx:
                if cur.next:
                    pre=cur
                    cur=nextn
                    nextn=nextn.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                pre.next=nextn
            else:
                return -1

    # Empty linked list
    def clear(self):
        self.head=None

    def print(self):
        cur=self.head
        string=""
        while cur:
            string +=str(cur.data)
            if cur.next:
                string+="->"
            cur=cur.next
        print(string)
