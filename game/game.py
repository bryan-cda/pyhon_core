import random

print('#######################')
print('       Python Game')
print('#######################')

message = 'hello world'
country = 'from Brasil'


print(message,country, sep=" - ", end="\n")

magical_number = int(random.randrange(10))
attempt = 3
round_game = 1

print('difficulty levels: ')

print('type 1 to easy, 2 to medium and 3 for hard')

d = int(input('Select difficulty level:'))

if d == 1:
    attempt = 20
else:
    if d == 2:
        attempt = 10
    elif d == 3:
        attempt = 5


def get_bonus():
    return magical_number * 2


for round_game in range(1, attempt + 1):

    print("Round {} of {}".format(round_game, attempt))

    i = int(input('type a magical number between 1 and 10: '))

    if i < 1 or i > 10:
        print('Invalid number, type number between 1 and 100!')
        continue

    if i == magical_number:
        print('Congratulations, this is the secret number')
        print('Your premium is {} {:.2f}'.format('R$', get_bonus() ))
        break
    else:
        if i > magical_number:
            print('Wrong, the passed number is major than secret number')
            continue
        elif i < magical_number:
            print('Wrong, the passed number is minor than secret number')
            continue

print('end of game.')
print()





