from collections import deque
stack = deque()
new_string = ''
string = 'We will conquere COVID-19'
for i in string:
    stack.append(i)
stack.reverse()
for i in stack:
    new_string += i
print(stack)
print(new_string)

def is_balanced(expression):
    stack1 = deque()
    brack_dict = {')':'(','}':'{',']':'['}
    for char in expression:
        if char in '({[':
            stack1.append(char)
        elif char in ')}]':
            if not stack1 or brack_dict[char]!= stack1.pop():
                return False
            

    return not stack1 #return not stack means if the stack is empty or not, if it is empty it will return it as true or else you will get it as false
            
a = is_balanced("({[a+b")
print(a)