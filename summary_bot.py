s = 0
while s >= 0:
    a = (input('Please input numeric (sum/clear/exit/quit): '))
    if a == 'sum':
        print('summary:', s)
        s = 0
        continue
    elif a == 'quit' or a == 'exit':
        print('Good buy')
        exit()
    elif a == 'clear':
        print('All clear!')
        s = 0
        continue
# защита от неверного ввода
    try:
        a = int(a)
        s = s + a
        print('accept')
    except ValueError:
        print('You missed, try again!')
