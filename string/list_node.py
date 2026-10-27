

class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def __str__(self):
        return f"[{self.value}, {self.next == None}]"

def print_list(f):
    p = f
    while p is not None:
        print(p.value, end="->")
        p = p.next
    print("\\")


def print_list2(f):
   p = f
   while p is not None:
        print(p.value*2, end="->")
        p = p.next

def create():
    j = 2
    head = ListNode(1, None)
    i = head
    while j < 11: 

        i.next = ListNode(j, None)
        i = i.next
        j += 1
    return head

def duplicate(head):
    head2 = ListNode(2*head.value, None)
    i = head2.next
    j = head.next
    print(head2, head, i, j)
    # while j is not None:

 