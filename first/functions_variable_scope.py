a = 12345

#if a variable is created outside a function and above it then the fuctions below can use that variable

def corn():
    print(a)
def buff():
    print(a)
def ass():
    a=67890
    print(a)


corn()
buff()
ass()