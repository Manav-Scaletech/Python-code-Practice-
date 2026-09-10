#class method in decorator : 
class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
s = Student()

s.show_school()