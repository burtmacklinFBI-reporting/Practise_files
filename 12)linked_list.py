class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev



class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        return self.head.data
          

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''
       

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
            
         
        print(llstr)
   
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)


    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def len_ll(self):
        count = 0
        itr = self.head
        while itr.next:
            count +=1
            itr = itr.next

        return count

    def remove_at(self,index):
        if index < 0 or index > self.len_ll():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count +=1 


    def insert_at(self,index,data):
        if index < 0 or index > self.len_ll():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def insert_after_value(self,data_after = None,data_to_insert = None):
        if self.head is None:
         return
        
        if data_after is None:
            node = Node(data_to_insert,self.head)
            self.head = node
            return self.head.data
        
        if data_to_insert is None:
            print('Please enter a value to insert')

        itr = self.head
        while itr:
         if itr.data == data_after:
             itr.next = Node(data_to_insert,itr.next)
             break
                         
         itr = itr.next

    def remove_by_value(self,data):
       if self.head is None:
         return
       
       if self.head.data == data:
            self.head = self.head.next
            return

       itr = self.head
       while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


    def print_forward(self):
    
        if self.head is None:
            print("Linekd List is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

            last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    
        
            



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
  
