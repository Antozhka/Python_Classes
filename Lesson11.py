from random import randint

def password_creator(min, max):# рекурсией
    simb = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    pswrd = ''
    pswrd_len = randint(min, max)
    for i in range(pswrd_len):
        pswrd += simb[randint(0, len(simb)-1)]
    count_upper = 0;
    count_lower = 0;
    count_digit = 0;
    for i in pswrd:
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lower += 1
        if i.isdigit():
            count_digit += 1
    if count_digit and count_lower and count_lower:
        return pswrd
    else:
        return password_creator(min, max)

print(password_creator(3, 5))
print(password_creator(3, 6))
print(password_creator(5, 10))

def password_creator_new(min, max):# через цикл while
    simb = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    pswrd = ''
    pswrd_len = randint(min, max)
    while not pswrd:
        for i in range(pswrd_len):
            pswrd += simb[randint(0, len(simb)-1)]
        count_upper = 0;
        count_lower = 0;
        count_digit = 0;
        for i in pswrd:
            if i.isupper():
                count_upper += 1
            if i.islower():
                count_lower += 1
            if i.isdigit():
                count_digit += 1
        if count_digit and count_lower and count_lower:
            return pswrd
        else:
            pswrd = ''


print(password_creator_new(3, 5))
print(password_creator_new(3, 6))
print(password_creator_new(5, 10))

def draw_board(x):
    for i in range(x):
        print(x * (' ' + x * '-'))
        print((x + 1) * ('|' + x * ' '))
    print(x * (' ' + x * '-'))
    return None

draw_board(3)

def common_elems(x, y):
    res=[]
    for i in x:
        for j in y:
            if i==j and not j in res:
                res.append(i)
                break
    return res

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common_elems(a, b))

def bulls_cows():
    x = randint(1000, 9999)
    x = str(x)
    print(x)
    print('Добро пожаловать!\nВведите 4-х значное число')
    y = input()
    while x!=y:
        bulls = 0
        cows = 0
        for i in range(len(x)):
            for j in range(len(y)):
                if i == j and x[i] == y[j]:
                    bulls += 1
                elif x[i] == y[j]:
                    cows += 1
        print('{} коров и {} быков'.format(cows, bulls))
        y = input()
    return 'Правильно! Игра окончена'

print(bulls_cows())