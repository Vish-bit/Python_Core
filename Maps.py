num = [1,2,3,4,5,6,7,8,9]
list(map(lambda x:x*x, num))


num1 = [1,2,3,4]
num2 = [5,6,7,8]
list(map(lambda x, y:x*y, num1, num2))

# Use map to convert strings to integers
str_num = ['1','2','3','4','5']
int_num = list(map(int, str_num))

print(int_num)


# use map for uppsercase conversion

fruits = ['apple', 'banana', 'orange', 'kiwi']
print(list(map(str.upper, fruits)))

# Use map for printing all names from array of objects
def get_name(person):
    return person['name']

people = [
    {'name': 'Visha', 'age': 26},
    {'name': 'Sagar', 'age':28}
]
print(list(map(get_name, people)))