#heirarchical inheritance


class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")

# Create instances of Child1 and Child2
child1 = Child1()
child2 = Child2()

child1.parent_method()  # Inherited from Parent
child1.child1_method()  # Specific to Child1
child2.parent_method()  # Inherited from Parent
child2.child2_method()  # Specific to Child2