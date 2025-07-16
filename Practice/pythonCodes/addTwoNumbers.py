class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def addTwoNumbers(list1, list2):
    dummyNode = listNode()
    currentNode = dummyNode
    carryNode = 0
        
    while list1 or list2 or carryNode:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0

            total = val1 + val2 + carryNode
            carryNode = total // 10
            currentNode.next = listNode(total % 10)
            currentNode = currentNode.next

            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
    return dummyNode.next
    

# this helper function is convert to list to linked list
def list_to_linked_list(numbers):
    dummyNode = listNode()
    currentNode = dummyNode
    
    for num in numbers:
        currentNode.next = listNode(num)
        currentNode = currentNode.next
    return dummyNode.next

# this helper function is convert linked list to list
def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

list1 = list_to_linked_list([2, 4, 3])
list2 = list_to_linked_list([5, 6, 4])
res = addTwoNumbers(list1, list2)
print(linked_list_to_list(res))