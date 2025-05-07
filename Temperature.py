# Create a program that converts temperatures between Fahrenheit and Celsius.
import math

while True:
    temp = float(input('\nEnter temperature: '))
    choice = int(input('\n1 Fahrenheit to Celsius, \n2 Celsius to Fahrenheit, \nSelect a conversion type: '))

    if choice == 1:
        celsius = math.ceil((temp - 32) * 5/9)
        print(f'\nConverted temperature: {celsius} oC')
    elif choice == 2:
        fahrenheit = math.ceil((temp * 9/5) + 32)
        print(f'\nConverted temperature: {fahrenheit} oF')
    else:
        print('Invalid selection')