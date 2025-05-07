class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("이전 노드가 리스트에 존재하지 않습니다.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def delete_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete(self, prev_node):
        if not prev_node or not prev_node.next:
            print("삭제할 노드가 존재하지 않습니다.")
            return
        to_delete = prev_node.next
        prev_node.next = to_delete.next
        if to_delete.next:
            to_delete.next.prev = prev_node


    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("NULL")


llist = DoublyLinkedList()
print("[첫 위치 삽입]")
for i in range(5):
    llist.insert_first(i)
    llist.print_list()
    if i == 2:
        temp = llist.head

print("[중간 위치 삽입]")
llist.insert(temp, 100)
llist.print_list()

print("[중간 위치 삭제]")
llist.delete(temp)
llist.print_list()

print("[첫 위치 삭제]")
for i in range(5):
    llist.delete_first()
    llist.print_list()