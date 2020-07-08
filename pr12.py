from pr11 import SingletonObject

obj1 = SingletonObject()
obj1.filename = "log_single.txt"

obj1.critical("test critical in singleton")
