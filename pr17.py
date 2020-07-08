class Book():

    _shared_state = {}

    # def sample(n = [])

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

a1 = Book()
a2 = Book()
a1.x = 200
a1.y = 500
a1.z = "Deep learning"
a2.w = "Mehrdad"
a3 = Book()
print("Book obj 'a1' :", a1)
print("Book obj 'a2' :", a2)
print("Book obj 'a3' :", a3)
print("obj state 'a1' :", a1.__dict__)
print("obj state 'a2' :", a2.__dict__)
print("obj state 'a3' :", a3.__dict__)
