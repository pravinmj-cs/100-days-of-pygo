print('''
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

 ''')
print("\n What can be an exercise without Calculator Program")


def ops(num1, num2, operator):
    opvalues = {1: '+', 2: '-', 3: '*', 4: '/'}
    if opvalues[operator] == '+':
        output = str(num1 + num2)
    elif opvalues[operator] == '-':
        output = str(num1 - num2)
    elif opvalues[operator] == '*':
        output = str(num1 * num2)
    elif opvalues[operator] == '/':
        output = str(num1 / num2)
    else:
        output = 'valid operator required'
    return output


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = 0
    while op not in range(1, 5):
        value = input(''' 
Pick up an operation:
    1. + (Add_
    2. - (Subtract)
    3. * (Multiply)
    4. / (Divide)

Type between 1 to 4
        ''')

        op = int(value)
    print("\n", ops(num1, num2, op))
except ValueError:
    print("Enter valid numbers")
    exit()
