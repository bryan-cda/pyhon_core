
#created list of musics for Lana del Rey

lanadelreyplaylist = ['born to die', 'love', 'summertime sadness', 'west coast']
#created variable for the full name of my wife

dualipaplaylist = ['new rules', 'new love', 'be the one']
name = 'Irys. da Silva. Batista. Lopes. Duarte. Albuquerque'
#printed full name of my wife sapareted for point

print(name.split('.'))
#printed my list in first position
firstmusic = lanadelreyplaylist[0]

print(firstmusic)

print('\n')
#printed my list in your four positions

print(lanadelreyplaylist[0:4])

#droped the last term of my list
lanadelreyplaylist.pop()

#add a new term of my list
print(lanadelreyplaylist + ['oi'])

#droped the last term of my list
lanadelreyplaylist.pop()

#used the append() method for add one more item of my list
lanadelreyplaylist.append('blue jeans')

#printed the new list
print(lanadelreyplaylist)

#changed to reverse my list
lanadelreyplaylist.reverse()

#printed the new list format
print(lanadelreyplaylist)

#used the sort() method for ordered the list
lanadelreyplaylist.sort()

print(lanadelreyplaylist)

#join the lana del rey's list with dua lipa's list
newlist = (dualipaplaylist+lanadelreyplaylist)

print(newlist)
#ordered the new list
newlist.sort()

#printed new list
print(newlist)

