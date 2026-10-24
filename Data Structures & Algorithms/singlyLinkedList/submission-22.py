class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self,head=None,tail=None):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        
        curr = self.head.next
        i = 0 
        while curr:
            if index  == i:
                return curr.val
            else:
                i+=1
            curr = curr.next 
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
         
        if not new_node.next:
            # list was empty, so this is also the tail
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        listNode = ListNode(val)
        self.tail.next = listNode
        self.tail = listNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:

        curr = self.head.next

        values_list = []
        while curr:
            values_list.append(curr.val)
            curr = curr.next
        return values_list
