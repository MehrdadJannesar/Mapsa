def arg_kwargs(**kwargs):

    # x = 5 --> {x:5}

    if kwargs is not None:
        for key,value in kwargs.items():
            print("{} == {}".format(key, value))

arg_kwargs(fname = "Ali", lname = "Dashti", age = 26)
# {fname : "Ali", lanme: "Dashti", age: 26}
