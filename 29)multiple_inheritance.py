class Father():
    def gardening(self):
        print('I enjoy gardening')

class Mother():
    def cooking(self):
        print('I love cooking')

class Child(Father,Mother): #this child is a derived class and father and mother are supposed to be the parent class
#This is multiple level inheritance
    def sports(self):
        print('I enjoy sports')

c = Child()
c.gardening()
c.cooking()
c.sports()


class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()