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
    print(num,'! = ', result)
    return result

findFactorial(10)
findFactorial(3)
findFactorial(4)

