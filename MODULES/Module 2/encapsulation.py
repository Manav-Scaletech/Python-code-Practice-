class Student:

    def __init__(self):
        self._name = "Manav"

    def get_name(self):
        return self._name
        


s = Student()
print(s.get_name())