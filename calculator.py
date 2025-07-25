a = float(input('enter a number:'))
b = input('enter an assignment operator ; +,-, *,/:')
c = float(input('enter a second number:'))

if b == '+':
    print(f'{a} + {c} = {a + c}')
elif b == '-': 
    print(f'{a} - {c} = {a - c}')
elif b == '*':          
    print(f'{a} * {c} = {a * c}')               
elif b == '/':
    if c != 0:
        print(f'{a} / {c} = {a / c}')
    else:
        print("Error: Division by zero is not allowed.")