list = ['Irys', 'Bryan', 'Ellora', 'Vaquinha', 'Megan']
print(len(list))
#access to the last element of list
print(list[-1])
#access to the first element of list
print(list[-len(list)])
#insert element on list with position
list.insert(3,'Keli')
print(list)
#insert element on last position of list
list.append('Kelvin')
print(list)
#search index of element
print(list.index('Kelvin'))
#remove element of list
list.pop(list.index('Kelvin'))
print(list)
list.sort()
print(list)
#count occurrence of list
print(list.count('Bryan'))

