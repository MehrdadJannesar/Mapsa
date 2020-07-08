
#1 __new__(cls)
#2 __init__(self)
#3 __call__(cls)

class A:

    def __init__(self):
        print("init")

    def __call__(cls):
        print("call")


a = A()
a()
