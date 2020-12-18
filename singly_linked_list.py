class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):    # At the end of list
        if self.head is None:
            self.head = new_node
        else:    # Traverse to end of list
            # self.head.next = new_node
            last_node = self.head
            while True:
                if last_node.next is None:
                    break    # While loop breaks
                last_node = last_node.next    # Points to None
            last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while True:
            if cur_node is None:
                print('List is empty!')
                return
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_at_head(self, new_node):
        cur_head = self.head
        self.head = new_node
        self.head.next = cur_head


if __name__ == "__main__":
    # Node=> data, next
    # firstNode.data => John, firstNode.next => None
    first_node = Node("John")    # Created node
    linked_list = LinkedList()    # Created linked list
    linked_list.append(first_node)    # Insert node - head=>John=>None
    second_node = Node("Ben")
    linked_list.append(second_node)    # Insert node - head=>John=>Ben=>None
    third_node = Node("Matt")
    linked_list.insert_at_head(third_node)
    linked_list.print_list()
