class node:
    def __init__(self, data=None):
        self.data = data #stores the past data point
        self.next = None #stores the pointer to next data point; set to None by default

class linked_list:
    '''
    A wrapper that wraps the nodes
    User interphases with this class
    '''
    def __init__(self):
        self.head = node() # placeholder to point to the first element in the list
    
    def append(self, data):
        '''
        create first element in the list
        '''
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        '''
        Determine length of linked list
        '''
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        '''
        display contents of linked list
        '''
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self,index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1
    
    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.erase(1)
my_list.display()

print('Element at 2nd Index: {index}'.format(index = my_list.get(1)))