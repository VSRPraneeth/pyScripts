from operator import itemgetter

users = [
    {'fname' : 'TOM', 'lname' : 'BROWN'},
    {'fname' : 'JIM', 'lname' : 'CARROT'},
    {'fname' : 'TRACY', 'lname' : 'TYPHOON'},
    {'fname' : 'DONALD', 'lname' : 'ASS'},
    {'fname' : 'KATIE', 'lname' : 'REYNOLDS'},
    {'fname' : 'BRYAN', 'lname' : 'BURTINOD'},
    {'fname' : 'TAYLOR', 'lname' : 'SWIFT'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('---------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
