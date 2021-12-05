# Identical Linked Lists

# Two Linked Lists are identical when they have the same data and the arrangement of data is also the same. For example, Linked lists a (1->2->3) and b(1->2->3) are identical. . Write a function to check if the given two linked lists are identical. 

class Node :
    def __init__ ( self , d ) :
        self.data = d
        self.next = None
 
class LinkedList :
    def __init__ ( self ) : self.head = None

    def areIdentical ( self, listb ) :
        a = self.head
        b = listb.head
        while ( a != None and b != None ) :
            if a.data != b.data : return False
            a = a.next
            b = b.next
            
        return ( a == None and b == None )

    def push ( self , new_data ) :
        new_node = Node ( new_data )
        new_node.next = self.head
        self.head = new_node
 
llist1 = LinkedList ()
llist1.push ( 1 )
llist1.push ( 2 )
llist1.push ( 3 )

llist2 = LinkedList ()
llist2.push ( 1 )
llist2.push ( 2 )
llist2.push ( 3 )
 
if llist1.areIdentical(llist2) == True : print( "Identical" )
else : print( "Not identical" )