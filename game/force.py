import random

line = open("bijus", "r")
bijus = []

for i in line:
    bijus.append(i.strip())
    print(bijus[random.randrange(0,len(bijus))])

line.close()


def force():
    # SETUP
    win = False
    lose = False
    word = bijus[random.randrange(0, len(bijus))]
    point = 0
    error = 0
    attempt = 5
    status = ['_' for i in word]

    opening_game()

    while not lose and not win:

        choice = input("try to discover letter: ")
        index = 0

        if choice in word:
            for letter in word:
                if letter.lower() == choice.lower():
                    print("discovered letter {} in position {} of the word".format(letter, index))
                    point = point + 1
                    status[index] = letter
                index = index + 1
        else:
            print("Wrong letter, try again!")
            error = error +1
            print("Total errors: ", error)
            print("Attempt remaining", attempt - error)
        lose = error == len(word)
        win = point == len(word)
        print("Total point number:", point)
        print('Status force: ', status)

        if win:
            print("You win!")
        elif lose:
            print("You lose! Try again!")
force()


def opening_game():
    print("************************")
    print("**** FORCE GAME ****")
    print("************************")

