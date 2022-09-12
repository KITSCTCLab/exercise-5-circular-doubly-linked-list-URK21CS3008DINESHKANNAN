class node:
    def __init__(s,x):
        s.data=x
        s.prew=None
        s.next=None
        
class DLL:
    def __init__(s):
        s.head=None
        
    def insertfront(s,x):
        new_node=node(x)
        if s.head !=None:
            new_node.next=s.head
            s.head.prew=new_node
        s.head=new_node
    def display(s):
        if s.head==None:
        print("Empty list")
        return
      t=s.head
    while t.data!=None:
          print(t.data,end="-->")
        t=t.next
         print("None")
    def delete(s,x):x
        if s.head==None:
        t=s.head
    while t.data !=x:
            t=t.next
        t.prev.next=t.mext
        t.prev.prev=t.prev

list1 =DLL ()
list1.insertfront(50)
list1.insertfront(40)
list1.insertfront(30)
list1.insertfront(20)
list1.display()
