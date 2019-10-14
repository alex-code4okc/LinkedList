'''
    Linked list implementation in python. 
'''
class LinkedList(object):
    class Node(object):
        def __init__(self,item,prev_node=None,next_node=None):
            self.item = item
            self.prev_node = prev_node
            self.next_node = next_node

    def __init__(self):
        self.linkedlist = []
        self.head = self.Node(None)
        self.tail = self.Node(None)
        #self.current = Node(None)
        self.count = 0

    def insert(self,item):
        # insert will always append to end of linked list
        node = self.Node(item)
        self.count += 1
        # if self.tail.prev_node points to None the linked list was empty and this insert is the first
        if(self.tail.prev_node is None):
            self.head.next_node = node
            self.tail.prev_node = node
        else: # this insert is not the first, tail points to a node
            self.tail.prev_node.next_node = node # previous last node now points its next_node to new node
            node.prev_node = self.tail.prev_node # new node prev_node now points to the previous last node
            self.tail.prev_node = node # tail prev_node now points to new node

    def getFirst(self):
        if(self.count == 0):
            return "Linked List is empty!"
        return self.head.next_node.item

    def getLast(self):
        if(self.count == 0):
            return "Linked List is empty!"
        return self.tail.prev_node.item

    def Count(self):
        return self.count

    def __str__(self):
        if(self.head.next_node is None):
            return "Linked List is empty!"
        else:
            accumulator = ""
            current_node = self.head.next_node
            while(current_node is not None):
                accumulator += str(current_node.item)
                if(current_node.next_node is not None):
                    accumulator += ", "
                current_node = current_node.next_node
        
            return accumulator


# TODO: InsertInto method to insert Node into 

# TODO: RemoveFirst method to return the first Node item

# TODO: Add RemoveFrom method to remove a node from specified index
    def removeFirst(self):
        if(self.isEmpty()):
            print("List is empty! No elements to remove.")
        else:
            # list is not empty
            if(self.Count() == 1):
                self.head.next_node = None
                self.tail.prev_node = None
            else:
                # list contains more than 1 node
                temp = self.head.next_node
                new_first_node = temp.next_node
                self.head.next_node = new_first_node
                new_first_node.prev_node = None
                temp.next_node = None
                self.count -= 1
# TODO: RemoveLast method to return the last Node item
    def removeLast(self):
        if(self.isEmpty()):
            print("List is empty! No elements to remove.")
        else:
            # list is not empty
            if(self.Count() == 1):
                # head and tail node point to the same node
                self.head.next_node = None
                self.tail.prev_node = None
                self.count -= 1
            else:
                # list has more than 1 node
                temp = self.tail.prev_node
                new_last_node = temp.prev_node
                self.tail.prev_node = new_last_node
                new_last_node.next_node = None
                temp.prev_node = None
                self.count -= 1            


    def isEmpty(self):
        return self.count == 0