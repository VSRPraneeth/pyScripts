class Girl:
    gender = "Female"                     #class variable

    def __init__(self, name):
        self.name = name                  #instance variable

r = Girl('Rachel')
s= Girl('Sammy')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
