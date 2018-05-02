class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def serialize(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def deserialize(array):
    res = ListNode(0)
    node = res
    for i in array:
        node.next = ListNode(i)
        node = node.next
    return res.next

