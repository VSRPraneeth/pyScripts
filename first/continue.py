numbersTaken = [2, 5, 12, 33, 17]

print("Here are the numbers that are still available :")

for x in range(1,20):
    if x in numbersTaken:
        continue
    print(x)
    # continue will skip the statements after continue and goes to the next number

'''
for a in range(1,20):
    if a not in numbersTaken:
        print(a)
'''


