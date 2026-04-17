class Node:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number
        self.next = None
        
    def __str__(self):
        return f"{self.letter}:{self.number} "
