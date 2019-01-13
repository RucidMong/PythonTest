my_dict = {}
my_dict[1] = 'a'
my_dict['b'] = 2
my_dict['c'] = 'd'

print(my_dict['c'])

students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
print(students)
for key in students.keys():
    print(key)

for key, val in students.items():
    print(key, val)

def add_mul(num1, num2):
    return num1+num2, num1*num2

my_add = add_mul(2, 3)
print(my_add)
print(type(my_add))
my_add[1] = 1