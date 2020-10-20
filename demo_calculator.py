"""Code that performs a calculation between two numbers. Next implementation for this code: unlimited number of inputs. This code has educational purposes; no copyright infringement is intended."""

while True:
    print("\nInstructions")
    print("Enter '+' if you want to add your inputs")
    print("Enter '-', if you want to subtract your inputs")
    print("Enter '*' if you want to multiply your inputs")
    print("Enter '/' if you want to divide your inputs")
    print("After you enter any of these symbols, you will be prompted to enter the inputs")
    print("Enter 'quit' to end the program")
    user_input = input(' ')

    if user_input == 'quit':
        break
    elif user_input == '+':
        num1 = float(input('Enter your first input: '))
        num2 = float(input('Enter your second input: '))
        answer = str(num1 + num2)
        print('The answer is ' + answer)
    elif user_input == '-':
        num3 = float(input('Enter your first input: '))
        num4 = float(input('Enter your second input: '))
        answer = str(num3 - num4)
        print('The answer is ' + answer)
    elif user_input == '*':
        num5 = float(input('Enter your first input: '))
        num6 = float(input('Enter your second input: '))
        answer = str(num5 * num6)
        print('The answer is ' + answer)
    elif user_input == '/':
        num7 = float(input('Enter your first input: '))
        num8 = float(input('Enter your second input: '))
        answer = str(num7 / num8)
        print('The answer is ' + answer)
    else:
        print('Unknown input')
