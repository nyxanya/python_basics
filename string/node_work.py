
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f"[{self.value}, {self.next == None}]"

def print_list(f):
    p = f
    while p is not None:
        print(p.value, end="->")
        p = p.next
    print("\\")

def remove_every_other_node(head):
    while head is not None:
        if head.next is not None:
            head.next = head.next.next
            head = head.next
        else:
            break

def remove_even_valued_nodes(head):
    p = ListNode(20)
    p.next = head
    while p.next is not None:
        if p.next.value%2 == 0:
           p.next = p.next.next
        else:
            p = p.next
        

def remove_odd_value(head):
    h = ListNode(20)
    h.next = head
    while head is not None:
        if head.next.value % 2 == 1:
            h.next = h.next.next
        else:
            h = h.next

           



def main():
    head = ListNode(1)
    p = head
    for i in range(2,12):
        p.next = ListNode(i*2)
        p = p.next
    print_list(head)

    remove_even_valued_nodes(head)
    
    

    print_list(head)

    p = head
    for i in range(2,15):
        p.next = ListNode((i*29) % 101)
        p = p.next
    print_list(head)

    
    remove_even_valued_nodes(head)
    
    print_list(head)

    remove_odd_value(head)
    print_list(head)

if __name__== "__main__":
     main()