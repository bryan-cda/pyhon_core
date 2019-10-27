print (1 in (1,2,4))

print (88 in range(1,189))

list1 = ('Bryan', 'Rafael', 'Leonardo')
list2 = ('Bryan', 'Rafael', 'Leonardo')

if print(list1 in list2):
    print('true')
else:
    print('not in here')

name = (input("Digite sua credencial para acessar Familia Lopes Duarte: "))

family  = ['Bryan', 'Irys', 'Ellora']
try_to = 0

while(True):
    if(name in family):
        print('Bem vindo de volta ao sistema da familia Lopes Duarte,', name)
        break
    elif(name not in family):
        print('Acesso negado.')
        tentativa +=1
        continue
        if(tentativa>=3):
            break

