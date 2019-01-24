def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age
'''
my_limit = allowed_dating_age(23)
joes_limit = allowed_dating_age(49)
print("I can only date ", my_limit, "or older")
print("Joe can only date ", joes_limit, "or older")
'''
for age in range(15,60):
    print("My age is ", age, " and I can date girls older than", allowed_dating_age(age), " years")


