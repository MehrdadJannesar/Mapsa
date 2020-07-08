def arguments(fname, *args):
    print("first Arg = ", fname)
    for arg in args:
        print("*args is : ", arg)

arguments('Mehrdad', 'cat', 'dog', 100, 20.2, 100.00000003)
