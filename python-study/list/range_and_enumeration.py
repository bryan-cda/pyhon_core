custom_list =[1990, 2001, 1993, 1989]
for i in range(len(custom_list)):
    value = custom_list[i]
    value += 1000
    print(value)

for index, i in enumerate(custom_list):
    i = custom_list[index]
    i += 2000
    print(i)