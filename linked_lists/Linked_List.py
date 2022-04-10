class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    
    def Insert(self, val_before, newdata):
        if val_before is None:
            print('No node to insert after')
            return
        else:
            new_node = Node(newdata)
            cur_value = 0
            cur_node = self.headval
            while True:
                last_node = cur_node
                cur_node = cur_node.nextval
                if cur_value == val_before:
                    last_node.nextval = new_node
                    new_node.nextval = cur_node
                    return
                cur_value += 1


list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
e6 = Node("Weds")
list.headval.nextval = e2
e2.nextval = e3
# e2.nextval = e6
e3.nextval = e4
e4.nextval = e5

list.InBetween(Node("Tue"), "Node(10)")


list.AtEnd("Sun")
list.Insert(1, 'Weds')

list.listprint()
