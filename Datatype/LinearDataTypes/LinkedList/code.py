class Node:
    def __init__(self,data):
        self.data = data
        self.next=None # setting pointer to None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def inserAtBeginning(self,new_data):
        node=Node(new_data)
        node.next=self.head #set the current node's head
        self.head=node #set the current node's head
        
    
    def inserAtEnd(self,new_data):
        node=Node(new_data)
        if self.head is None:
            node.next=self.head
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=node
        
    def deleteFromBeginning(self,new_data):
        node=Node(new_data)
        if self.head is None:
            return ("Node is empty")
        self.head=self.head.next
            
        self.head=self.head
        
    def deleteFromEnd(self,new_data):
        node=Node(new_data)
        
        start=self.head
        
        while start.next.next:
            start=start.next
        start.next=None
        
    def retrieveSpecificValues(self,value):
        start=self.head
        position=0
        while start:
            if start.data == value:
                print(f"item {start.next} retrieved at position {position}")
            start=start.next
            position+=1
        return f"Value '{value}' not found in the list" 
    
    
    def getSizeOfLList(self):
        start=self.head
        counter=0
        while start is not None:
            counter+=1
            start=start.next
        return counter
    
    def checkIfEmpty(self):
        if self.head is None:
            return True
        
    def valueAtIndex(self, index):
        start=self.head
        position=0
        while start is not None:
            if position==index:
                return start.data
            start=start.next
            position+=1
           
        return None     

        
    
    def __str__(self):
        nodes=[] 
        current=self.head
        while current:
            nodes.append(str(current.data))
            current=current.next
        return " -> ".join(nodes) + " -> None"  # Join all node data with " -> " and add " -> None" at the end.

        
    
llist = LinkedList()

print("calling inserAtBeginning",llist.inserAtBeginning("Potato"))
print("calling inserAtBeginning",llist.inserAtBeginning("Avocado"))
print("calling inserAtBeginning",llist.inserAtBeginning("Pawpaw"))
print("calling inserAtEND",llist.valueAtIndex(2))
print("calling search method",llist.checkIfEmpty())





print("new llist after inserAtBeginning",llist)

