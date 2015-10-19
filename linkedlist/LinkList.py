from ListNode import ListNode


class LinkList(object):
    def __init__(self):
        self.__head = ListNode(None)

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.__head = node

    def get_tail(self):
        tail = self.__get_head__()
        while tail.next:
            tail = tail.next
        return tail

    def add(self, node):
        tail = self.get_tail()
        tail.next = node
        node.next = None

    def get_node(self, val):
        node = self.get_head()
        while node:
            if node.val == val:
                return node
            else:
                node = node.next
        return None

    def indexof(self, position):
        node = self.get_head()
        if position <= 0:
            return node
        else:
            count = 0
            while count < position and node:
                node = node.next
                count += 1
            if not node:
                return None
            elif count == position:
                return node
            else:
                return None

    def head_insert(self, node):
        head = self.get_head()
        node.next = head.next
        head.next = node
        self.set_head(head)

    def insert(self, node, position):
        head = self.get_head()
        node_pre = self.indexof(position - 1)
        if not node_pre:
            print('can not insert!!!')
        else:
            if node_pre == head:
                self.head_insert(node)
            else:
                node.next = node_pre.next
                node_pre.next = node

    def delete_node(self, node, position):
        head = self.get_head()
        node_pre = self.indexof(position - 1)
        if not node_pre:
            print('can not delete!!!')
        else:
            if node_pre == head:
                head.next = None
                self.set_head(head)
            else:
                node_pre.next = node.next


