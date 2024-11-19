def sum(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "\n I can't calculate by zero. \n "
    
def calculator():
    while True:
        print("\n Avaliable operations:")
        print("1. Sum")
        print("2. Multiply")
        print("3. Subtract")
        print("4. Divide")
        print("5. Exit\n ")

        choice = input(
            'Choice operation: 1, 2, 3, 4 or if you wanna exit 5: ')

        if choice == '5':
            print("\nThank you!\n")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Type a number: "))
                num2 = float(input("Type a number: "))

                if choice == '1':
                    print(f'\n **** {num1} + {num2} = {sum(num1, num2)} **** ')

                if choice == '2':
                    print(f'\n **** {num1} * {num2} = {multiply(num1, num2)} **** ')

                if choice == '3':
                    print(f'\n **** {num1} - {num2} = {subtract(num1, num2)} ****')

                if choice == '4':
                    print(f'\n **** {num1} / {num2} = {divide(num1, num2) }**** ')
            except:
                print("Enter a valid number, please.")
        else:
            print("\n ***INVALID CHOICE*** \n.")

calculator()
