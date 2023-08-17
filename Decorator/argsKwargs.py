def dummy_func(*args):
    print (args)

# * allows us to extract positional variables from an iterable when we are calling a function
dummy_func(*range(10))

def dummy_func_new(**kwargs):
    print (kwargs)

dummy_func_new(a=0, b=1)

# Similar to *args, you can use ** for definition.
new_dict = {'a': '10', 'b': '20'}

dummy_func_new(**new_dict)
