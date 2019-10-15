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
        self.head = self.Node(None)
        self.tail = self.Node(None)
        #self.current = Node(None)
        self.count = 0

    def insertLast(self,item):
        # insertLast will always append to end of linked list
        node = self.Node(item)
        
        # if self.tail.prev_node points to None the linked list was empty and this insertLast is the first
        if(self.tail.prev_node is None):
            self.head.next_node = node
            self.tail.prev_node = node
            self.count += 1
        else: # this insertLast is not the first, tail points to a node
            self.tail.prev_node.next_node = node # previous last node now points its next_node to new node
            node.prev_node = self.tail.prev_node # new node prev_node now points to the previous last node
            self.tail.prev_node = node # tail prev_node now points to new node
            self.count += 1

    def insertFirst(self,item):
        node = self.Node(item)
        if(self.isEmpty()):
            self.head.next_node = node
            self.tail.prev_node = node
            self.count += 1
        else:
            temp_node = self.head.next_node
            self.head.next_node = node
            node.next_node = temp_node
            temp_node.prev_node = node
            self.count += 1

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


# TODO: InsertInto method to insertLast Node into 
    def insertInto(self,item,index):
        '''
            Inserts element into the nth index (zero based index). 
            If list is empty, element will be inserted at the head/tail.
            0 index will insert at the head.
            -1 index will insert at the tail.
            index must be less than or equal to the number of currently linked nodes.
            If equal to the number of linked nodes, element is inserted at the end of the list.
            if the index is larger than the number of currently linked nodes, the node is not inserted.
        '''
        if(self.isEmpty()):
            self.insertLast(item) # first item in the list
        elif(index == 0):
            self.insertFirst(item)
        elif(index == -1):
            self.insertLast(item)
        elif(index == self.Count()):
            self.insertLast(item) # insertLast will insertLast to the end of the list
        elif(index < self.Count()):
            node = self.Node(item)
            current_index = 0
            current_node = self.head.next_node
            while(current_node.next_node is not None):
                current_index += 1
                current_node = current_node.next_node
                if(index == current_index):
                    temp_node = current_node
                    temp_node.prev_node.next_node = node
                    node.prev_node = temp_node.prev_node
                    node.next_node = temp_node
                    temp_node.prev_node = node
        else:
            print("Attempted to element beyond the length of the list")

# TODO: Add RemoveFrom method to remove a node from specified index

# TODO: RemoveFirst method to return the first Node item
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