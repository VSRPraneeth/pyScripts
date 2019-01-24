'''
tuna = int(input('What\'s your fav number?\n'))
print(tuna)
'''

while True:
    try:
        number = int(input('What\'s your fav number?\n'))
        print(18/number)
        break
    except ValueError:
        print('Please Enter a number')
    except ZeroDivisionError:
        print('Don\'t pick zero')
    except:
        break
    finally:
        print('loop completed')


