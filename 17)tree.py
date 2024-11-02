class TreeNode:
    def __init__(self,name):
        self.data = name
        self.child = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.child.append(child) 

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.child:
            for i in self.child:
             i.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()

class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.child = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.child.append(child) 

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self,parameter='both'):
        if parameter.lower() == 'name':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name)
            if self.child:
                for i in self.child:
                 i.print_tree(parameter)
        elif parameter.lower() == 'designation':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if self.child:
                for i in self.child:
                 i.print_tree(parameter)
        else:
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name + '(' + self.designation + ')')
            if self.child:
                for i in self.child:
                 i.print_tree(parameter)


def build_management_tree():
    root = TreeNode("Nilupul",'CEO')

    cto = TreeNode("Chinmay",'CT0')
    infra_head = TreeNode("Vishwa",'Infrastructure Head')
    cto.add_child(infra_head)
    infra_head.add_child(TreeNode("Dhaval",'Cloud Manager'))
    infra_head.add_child(TreeNode("Abhijit",'App Manager'))
    cto.add_child(TreeNode("Aamir",'Application Head'))
    
    hr = TreeNode("Gels",'HR Head')
    hr.add_child(TreeNode("Peter",'Recruitement Manager'))
    hr.add_child(TreeNode("Waqas","Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)
   
    return root

if __name__ == '__main__':
   root_node =  build_management_tree()
   root_node.print_tree('designation')


class TreeNode:
    def __init__(self,name):
        self.data = name
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child) 

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self, level):
            if self.get_level() > level:
                return
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(level)


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
   rootnode = build_location_tree()
   rootnode.print_tree(1)

