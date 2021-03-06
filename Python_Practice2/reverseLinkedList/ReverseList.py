# Python program to reverse a linked list 
# Time Complexity : O(n) 
# Space Complexity : O(1) 

# Node class
from typing import List


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        solution = []
        j = 0
        for i in nums:
            j += i
            solution.append(j)
        return solution


# Driver program to test above functions
if __name__ == '__main__':
    test = Solution()
    list2 = [1, 2, 3, 4, 5]
    listResult = test.running_sum(list2)
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Given Linked List")
    llist.printList()
    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()
    print("\nRunning total")
    print(str(listResult)[1:-1])
