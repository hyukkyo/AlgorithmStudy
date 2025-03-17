class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None # 헤드와
        self.tail = None # 테일이 있는 버전으로 짜볼예정
        self.size = 0
    
    def insert_back(self, value):
        new_node = Node(value, None)

        if self.head:
            self.tail.next = new_node # 기존 테일 뒤에 붙이기
            self.tail = new_node # 새 노드를 테일로 지정
        else: # 비어있으면
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def get(self, idx):
        if idx >= self.size: # out of range
            return
        
        current_node = self.head # 헤드부터 시작
        while idx > 0:
            current_node = current_node.next
            idx -= 1
            
        return current_node.value
        

    def insert_at(self, idx, value):
        new_node = Node(value, None)

        if idx == 0: # 맨앞에
            new_node.next = self.head
            self.head = new_node

        elif 0 < idx and idx < self.size:

            previous_node = self.head
            while idx > 1:
                previous_node = previous_node.next
                idx -= 1

            new_node.next = previous_node.next
            previous_node.next = new_node

        elif idx == self.size: # 맨뒤에
            self.insert_back(value)


    def remove(self, idx):
        if idx == 0: # 헤드삭제
            self.head = self.head.next

        elif 0 < idx and idx <= self.size:
            previous_node = self.head
            while idx > 1:
                previous_node = previous_node.next
                idx -= 1

            previous_node.next = previous_node.next.next

        elif idx == self.size:
            previous_node = self.head
            while idx > 1:
                previous_node = previous_node.next
                idx -= 1

            previous_node.next = None
            self.tail = previous_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
            

ll = LinkedList()
ll.insert_back(2)
ll.insert_back(7)
ll.insert_back(1)
ll.insert_at(1, 4)
ll.print()
ll.insert_back(5)
ll.print()
ll.remove(3)
ll.print()
print(ll.get(2))

# 노드가 next만 있는걸 singly 링크드리스트
# 노드가 next와 prev를 가지면 doubly 링크드리스트