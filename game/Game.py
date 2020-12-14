print('#######################')
print('       Python Game')
print('#######################')

message = 'hello world'
country = 'from Brasil'


print(message,country, sep=" - ", end="\n")

magical_number = 43

i = int(input('type a magical number: '))

if i == magical_number:
    print('Congratulations, this is the secret number')
elif i > magical_number:
    print('Wrong, the passed number is major than secret number')
elif i < magical_number:
    print('Wrong, the passed number is minor than secret number')
print('end of game.')
