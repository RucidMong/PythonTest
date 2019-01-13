import random
students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
fruits = ['사과', '딸기', '망고', '브로콜리', '바나나']

for i in range(1,6):
    print(random.choice(fruits))

my_fruit = random.sample(fruits, 2)
print(my_fruit)
print(type(my_fruit))

my_int = random.randint(0, 10)
print(my_int)

str1 = '연구소장 '
str2 = '서현호'
str3 = str1 + ''.join(str2)
print(str3)