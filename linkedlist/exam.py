from LinkList import LinkList

l1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
l2 = [2]

list1 = LinkList()
list2 = LinkList()

list1.from_list(l1)
list2.from_list(l2)

# print list2


def find(headA, headB):
    if not headA or not headB:
        return None
    nodeA = headA
    while nodeA.next:
        nodeA = nodeA.next
        print nodeA
    nodeA.next = headA
    slow = fast = headB
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:               
        nodeA.next = None
        return None
    slow = headB
    while slow != fast:
        slow = slow.next
        fast = fast.next
    nodeA.next = None
    return slow

node = find(list1.get_head(), list2.get_head())
print node
print list1
print list2
