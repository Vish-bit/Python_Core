#1 Reverse a string (list[<start>:<stop>:<step>])

def reverseStr(text):
    # print(text[::-1])+
    return text[::-1]

str1 = reverseStr("Hi I am Vishakha")


#2 Finding Prime number

def findPrime(num):
    if(num > 1):
        for i in range(2, num):
            if(num%i == 0):
                # print('Not a Prime')
                return
            # print('** Is a Prime Number **') 
            return 'Is Prime Number'
    else:
        # print('** Not a Prime number **')
        return
        
findPrime(24)


#3 Find Factorial (Iterative & Recursive)

def findFactorial(num):
    result = 1
    for i in range(1, num + 1):
        # print('result --> ',result, 'i --> ', i, 'num --> ', num)
        result = result * i
    # print(num,'! = ', result)
    return result

findFactorial(10)
findFactorial(3)
findFactorial(4)

#4 Fibonacci sequence in Stocks finance

def fibonacci_retracement(high, low):
    diff = high - low
    levels = {
        '0.0%': high,
        '23.6%': high - diff * 0.236,
        '38.2%': high - diff * 0.382,
        '50.0%': high - diff * 0.5,
        '61.8%': high - diff * 0.618,
        '78.6%': high - diff * 0.786,
        '100.0%': low
    }
    return levels

retracement_levels = fibonacci_retracement(227.10, 235.30)

#Printing levels
# for level, price in retracement_levels.items():
    # print(f"{level}: Inr {price:.2f}")


#5 Count vowels in a string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = []

    for char in string:
        if char in vowels:
            count.append(char)
    # print("Vowels Count --> ", len(count))
    return len(count)

count_vowels("Vishakha")

#6 Check Palindrome 
def check_palindrome(org_str):
    value = str(org_str).lower()
    reversed_value = value[::-1]
    if value == reversed_value:
        print(value, 'Palindrome')
        return 'Palindrome'
    else:
        print(value, 'Not a Palindrome')
        return 'Not a Palindrome'
    
check_palindrome("vishakha")
check_palindrome("Madam")
check_palindrome(10101)

