from node import Node

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self, letter, number):
        new_node = Node(letter, number)
        
        if not self.head:
            self.head = new_node
            return
            
        current = self.head 
        while current.next:
            current = current.next
            
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current,end="")
            current = current.next 

    def find(self,letter):
        current = self.head
        while current:
            if current.letter == letter:
                return current.number
            current = current.next
        return 0