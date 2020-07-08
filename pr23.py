class A:

    def __init__(self, a, b, c):
        pass

v = A(1,2,3)

class B:

    def __call__(cls,a, b, c):
        pass

z = B()
z(1,2,3)
