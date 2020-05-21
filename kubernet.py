class node(text):
    def __init__(self,text):
        self.text=text
        self.next=None



class secondNode():
    def __init__(self):
        self.head=None

    def addfornt(node):
        if head is None:
            head=node
            break
        node.next=head
        head =node

    def printlist():
        if head is None:
            print("List Empty")
        else:
            traverse=head
            while(traverse.next):
                print(traverse.text+ " ")
                traverse=traverse.next

    def addatend(node):
        if head is None:
            head=node
        else:
            traverse =head
            while(traverse.next):
                traverse=traverse.next
            traverse.next=node

    def addatindex(node,index):
        if index >0 :
            if index > listlength()+1:
                print('list indexed is not exitised')
            else:
                if index  == listlength()+1:
                    addatend(node)
                elif index ==1 and listlength()>0:
                    addfornt(node)
                else:
                    traverse =None
                    while(index-2):
                        traverse=traverse.next
                    node.next=traverse.next
                    traverse.next=node

    def deleteatstart():
        temp =head
        head =head.next
        temp.next=None


    def deleteatend():
        traverse =head
        length =listlength()
        while(length-2):
            traverse =traverse.head
            length--
        traverse.next=None



    def deleteatindex(index):
        if index>0:
            if index == listlength() and index is not int(1):
                deleteatend()
            elif index ==1 and listlength()>1:
                deleteatstart()
            else:
                traverse =head
                while(index-2):
                    traverse =traverse.next
                traverse.next=traverse.next.next
                traverse.next.next=None


    def  listlength():
        if head is None:
            return 0
        else:
            length=0
            traverse=head
            while(traverse.next):
                length++
                traverse=traverse.next
            return length

    def cratelist(index,value):
        traverse=head
        for x in range(index):
            if x ==1:
                e1= node(value[x])
                traverse =e1
            else:
                e1 =node(value[x])
                traverse.next=e1

        printlist()


def switch(x):
        if x ==1:
            es=secondNode()
            x = [int(x) for x in input("Enter List value: ").split()]
            es.cratelist(x.length,x)
        if x==2:
            



def menufunction():
    print("(1) Create A Linked List\n")
    print("(2) INSERT A NODE AT THE STARTING\n")
    print("(3) INSERT A NODE AT THE INDEX\n")
    print("(4) INSERT A NODE AT THE END\n")
    print("(5) PRINT THE ALL LINKIED LIST\n")
    print("(6) DELETE A NODE AT THE STARTING\n")
    print("(7) DELETE A NODE AT THE END\n")
    print("(8) DELETE A NODE AT THE STARTING\n")
    print("(9) DELETE THE WHOLE LIST\n")

    x = int(input("ENTER YOUR CHOICE HERE\n"))
    switch(x)










if __name__ == '__main__':
    menufunction()
