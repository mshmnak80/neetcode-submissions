class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur != self.tail and i < index:
            cur = cur.next
            i += 1

        if cur != self.tail and i == index:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node  = ListNode(val)

        # next =self.head.next 
        # prev = self.head
        
        # prev.next = node
        # next.prev = node
        # node.next = next
        # node.prev = prev
        
        #another way
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node # the existing node that happens to be after created node should also point to new node
        self.head.next = node


    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        node  = ListNode(val)
        cur = self.head
        while cur and index > 0:
            cur = cur.next
            index = index -1

        if cur and cur != self.tail and index == 0:
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node
        
            


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # cur.next is the node to delete, and it must be a real node, not the tail sentinel
        if cur and cur.next and cur.next != self.tail and index == 0:
            target = cur.next
            cur.next = target.next          # 1. node before skips over target
            target.next.prev = cur          # 2. node after points back to cur
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)