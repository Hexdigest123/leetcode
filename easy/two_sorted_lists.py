class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


arg_list1 = ListNode(1, ListNode(2, ListNode(3)))
arg_list2 = ListNode(1, ListNode(3, ListNode(4)))


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    linked_list = ListNode()
    current = linked_list

    while list1 or list2:
        if list1 is None:
            current.next = list2
            list2 = list2.next
        elif list2 is None:
            current.next = list1
            list1 = list1.next
        elif list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    return linked_list.next


some_list = merge_two_lists(arg_list1, arg_list2)
while some_list:
    print(some_list.val)
    some_list = some_list.next