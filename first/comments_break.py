magicNumber = 26

# This is a one line comment

'''
This
is
a
multi-line
comment
'''

print(5+5)

print("Bucky" + "Roberts")

print("Bucky ", 9)

for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number")
        break
    else:
        print(n)

for MulOfFour in range(101):
    if MulOfFour % 4 is 0:
        print(MulOfFour)
    else:
        print(MulOfFour, "is not a multiple of four")


