class Parent:
    def __init__(self, name):
        print('Parent__init__', name)

class Parent2:
    def __init__(self, name):
        print('Parent2__init__', name)

class Child(Parent, Parent2):
    def __init__(self):
        print('Chile__init--')
      #  super().__init__('safdar')
        Parent2.__init__(self, 'Ali')
        Parent.__init__(self, 'Imran')

child = Child()
print(Child.__mro__)

