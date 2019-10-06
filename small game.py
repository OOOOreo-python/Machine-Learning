import random
secret = random.randint(1,10)
temp = input('输入一个数字')
guess = int(temp)
while(guess !=secret ):
    temp = input('重新输入一个数字')
    guess = int(temp)
    if guess == secret:
        print('yes')
    else:
        if guess > secret:
            print('big')
        else :
            print('small')
print('game over')