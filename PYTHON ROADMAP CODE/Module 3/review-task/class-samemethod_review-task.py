from typing import override


class A:
    def no(self, name):
        print("greet here A:")

class B:
    def no(self, name):
        print("greet here B:")
        print(name)

class C(A, B):
    @override
    def no(self, name):
        B.no(self, name)

c = C()
