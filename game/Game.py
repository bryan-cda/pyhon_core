print('#######################')
print('       Python Game')
print('#######################')

message = 'hello world'
country = 'from Brasil'


print(message,country, sep=" - ", end="\n")

magical_number = 43
attempt = 3
round = 1


while round <= attempt:

    print("Round {} of {}".format(round,attempt))

    i = int(input('type a magical number: '))

    if i == magical_number:
        print('Congratulations, this is the secret number')
        break
    else:
        if i > magical_number:
            print('Wrong, the passed number is major than secret number')
        elif i < magical_number:
            print('Wrong, the passed number is minor than secret number')
    print('end of game.')

    round = round +1