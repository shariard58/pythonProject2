class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: Node = None
        self.prev: Node = None


def print_forward(head: Node):
    while head.next:
        print(head.value)
        head = head.next
    print(head.value)


def print_backward(tail: Node):
    while tail.prev:
        print(tail.value)
        tail = tail.prev
    print(tail.value)


def add_to_first(head: Node, value: int):
    temp = Node(value)
    temp.next = head
    head.prev = temp
    return temp

def del_from_first(head:Node):
    head = head.next
    head.prev = None
    return head



print("Example")

if __name__ == '__main__':
    first = Node(1)
    second = Node(5)
    third = Node(7)
    forth = Node(10)

    first.next = second
    second.next = third
    third.next = forth

    forth.prev = third
    third.prev = second
    second.prev = first

    # print(" From start to end")
    # print_forward(first)
    # print("From end to start ")
    # print_backward(forth)
    #
    # temp1: Node = add_to_first(first, 14)
    # print("After Adding a new node befor head")

    # print_forward(temp1)

    # print_backward(forth)

    temp = del_from_first(first)
    print_forward(temp)




