class Node:
    def __init__(self, value):
        self.value:int = value
        self.next:Node = None
        self.prev:Node = None


def print_forwar(head:Node):
    while head.next:
        print(head.value)
        head = head.next

    print(head.value)


def print_backward(tail : Node):
    while tail.prev:
        print(tail.value)
        tail = tail.prev

    print(tail.value)

def add_to_the_first(head : Node, value: int):

    temp = Node(value)
    temp.next = head
    head.prev = temp

    return temp







if __name__ == '__main__':

    first = Node(1)
    second = Node(3)
    third = Node(8)
    forth = Node(14)
    fifth = Node(16)

    first.next = second
    second.next = third
    third.next = forth
    forth.next = fifth

    fifth.prev = forth
    forth.prev = third
    third.prev = second
    second.prev = first

print_forwar(first)


print("From End to Start")

print_backward(fifth)

