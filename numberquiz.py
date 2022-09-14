import random

number = random.randint(1, 100)
aa = 1

def num ():
    print ('1부터 100까지의 수를 맞춰 보세요!')
    a = int(input())
    if a == number:
        print ('축하합니다! 맞추셨네요.')
        exit()

    elif a > number:
        print ('down')
        num()

    elif a < number:
        print ('up')
        num()

    elif number > 100:
        print ('입력하신 수가 100보다 큽니다.')
        num()

num()

