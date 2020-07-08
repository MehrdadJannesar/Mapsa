# classmethod
class Triangle:

    area = 50

    @classmethod
    def printarea(cls):
        print("area is :" , cls.area)



# Triangle.printarea = classmethod(Triangle.printarea)
Triangle.printarea()
