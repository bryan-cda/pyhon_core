print('before for')
print(' ')
for i in range(10):
    print('inside for')
    print(i)
    if(i == 8):
        print('now is 8')
        break;
print('so, now we are out of for cause we break')