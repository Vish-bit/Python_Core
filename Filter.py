# Filter func constructs an iterator from elements of an iterable for which a func returns true.
# It is used to filter out items from a list based on a condition.

def even(num):
    if num % 2 == 0:
        return True
    
even(25)
even(24)

lst = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]

print(list(filter(even, lst)))

greater_num = list(filter(lambda num: num>10, lst))
print(greater_num)


# Filter with lambda and multiple conditions
greater_even_num = list(filter(lambda num: num>10 and num%2==0, lst))
print(greater_even_num)


#Filter to check if the age is greater than 25 in dictionaries

people = [
    {'name': 'Visha', 'age': 26},
    {'name': 'Sagar', 'age':28},
    {'name': 'Jack', 'age':32},
    {'name': 'John', 'age':23}
]

def age(person):
    return person['age']<25

print(list(filter(age, people)))

import numpy as np