
# SETUP

win = False
lose = False
word = "kurama"
point = 0
error = 0
attempt = 5
status = ['_','_','_','_','_','_']

print("************************")
print("**** FORCE GAME ****")
print("************************")
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
    lose = error == 6
    win = point == 6
    print("Total point number:", point)
    print('Status force: ', status)

    if win:
        print("You win!")
    elif lose:
        print("You lose! Try again!")


