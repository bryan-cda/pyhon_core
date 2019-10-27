credentials = {'id': '1', 'name':'Bryan', 'email':'bryan.duarte@celeritech.com.br'}

print(type(credentials))

print(credentials['name'] + ' E-mail: ' + credentials['email'])

employee = {"Nome":"Bryan", "CPF":"222.111.333-03", "Cargo":"Analista Desenvolvedor Pleno", "Estado Civil":"Casado", "Dependente":{"nome: Irys"}, "Filho":['Ellora']}

print(employee['Dependente'])
print(employee['Filho'])

print(employee.keys())

print(employee.items())