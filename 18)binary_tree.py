class BinarySeachTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySeachTree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySeachTree(data) # the important thing with recursion is that knowing when to exit from the loop

    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
             return self.left.search(val)
            else:
             return False
            
        if self.data > val:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_max(self):
        if self.data:
            if self.right:
                return self.right.find_max()
            else:
                return self.data
        
    def find_min(self):
        if self.data:
            if self.left:
                return self.left.find_min()
            else:
                return self.data
            

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal() # this is a way of appending to lists itseems.

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def calculate_sum(self):
       left_sum = self.left.calculate_sum() if self.left else 0
       right_sum = self.right.calculate_sum() if self.right else 0
       return self.data + left_sum + right_sum



    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
         elements=[]
         if self.left:
            elements += self.left.post_order_traversal()

         if self.right:
            elements += self.right.post_order_traversal()
 
         elements.append(self.data)
        
       
         return elements
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
        
        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)
       
        return self
#This is another way to remove from the left side. 
#  max_val = self.left.find_max()
#  self.data = max_val
# self.left = self.left.delete(max_val)
        
        
        
def buildtree(elements):
    print("building tree with this elements",elements)
    root = BinarySeachTree(elements[0])

    for i in range(1,10):
        root.add_child(elements[i])

    return root

def build_tree(elements):
    root = BinarySeachTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.inorder_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())