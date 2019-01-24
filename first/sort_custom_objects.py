from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('Cucky', 67),
    User('Block', 90),
    User('Amanda', 25),
    User('Sapphire', 45),
    User('Logic', 78),
    User('Dolly', 5),
    User('Goon', 32),
]

for x in users:
    print(x)

print('----------------')

for x in sorted(users, key=attrgetter('name')):
    print(x)

print('----------------')

for x in sorted(users, key=attrgetter('user_id')):
    print(x)