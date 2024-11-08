n = int(input().strip())
    
if 1<= n <=100:
    if n%2!= 0:
        print('Weird')
    elif n>1 and n<6:
        print('Not Weird')
    elif n>5 and n<21:
        print('Weird')
    elif n>20:
        print('Not Weird')
