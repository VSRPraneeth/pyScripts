date, item, price = ['june 26 2018', 'cigs', 9.05]
print(item)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([51, 35, 53, 23, 65, 46])
