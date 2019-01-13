# -*- coding: utf-8 -*-
#name = input('What is your name?')
#print(name, name)
bool1 = True
bool2 = False
bool4 = 1 < 2
bool5 = 1 == 2
print(bool1, bool2, bool4, bool5)

my_list = []
print(my_list)
my_list.append(123)
print(my_list)
my_list.append('abc')
print(my_list)
my_list.append(True)
print(my_list)

my_tuple = (1,'b')
print(my_tuple)
my_tuple = 3.14, 'Python', True
print(my_tuple)

my_dict = {}
print(my_dict)
my_dict[1] = 'a'
print(my_dict)
my_dict['b'] = 2
print(my_dict)
my_dict['c'] = 'd'
print(my_dict)

print(int(3.14))
print(float(3))
print(str(3.0))
print(type(str(3.0)))
print('3.0')
print(list('3.0'))

my_str = """버스
지하철
택시
"""
print(my_str)

print('My name is %s' % 'Tom')
print('x = %d, y = %d' % (1, 2))
print('%d x %d = %d' % (2, 3, 2*3))

print('%d %.2f' % (1,2))

print('My name is {}'.format('Hyun'))
print('{} x {} = {}'.format(2, 3, 2*3))
print('{1} x {0} = {2}'.format(2, 3, 2*3))
print('{2} x {1} = {2}'.format(2, 3, 2*3))

alphabet = 'abcde'
print(alphabet)
print(alphabet[2])

my_name = '연구소장 서현호'
print(my_name[1], '&', my_name[5], '&&', my_name[-1])
print(my_name[0:4])
print(my_name[:4])
print(my_name[5:8])
print(my_name[5:])

split_name = my_name.split()
print(split_name)
print(split_name[0])
print(split_name[1])

print(split_name[0])
print(split_name[0], end='/')
print(split_name[0])
print(split_name, end='희망')
print(split_name[0])

my_list = []
print(my_list)
print(type(my_list))
my_list.append(1)
my_list.append(3)
my_list.append(2)
print('*' * 30)
print(my_list)
print(my_list.sort())
print(my_list)
print(my_list.count(1))
print(type(my_list))
mine = 1
print(type(mine))
mine = 1, 2
print(type(mine))
mine = '1'
print(type(mine))
mine = '1', '2'
print(type(mine))
mine = [1]
print(type(mine))
my_tuple = (1, 2, 3)
print(my_tuple)
num1, num2, num3 = my_tuple
print(num1, num2, num3)
num1, num2 = num2, num1
print(num1, num2, num3)

animals = ['땅다람쥐', '바다코끼리', '스컹크', '아나콘다', '코알라', '하이에나', '바다소']
for animal in animals:
    print(animal)

for num in [1,2,3]:
    print(num)

for ch in '연구소장 서현호입니다.':
    print(ch, end='*')

for n in range(5):
    print(n)
print('*' * 30)
for n in range(3,5):
    print(n)

for i in range(2, 10):
    for j in range(1, 10):
        print('{0} x {1} = {2}'.format(i, j, i*j))

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [i for i in range(1, 20) if i % 2 == 1]
print(numbers)
odd_numbers = []

print(odd_numbers)
for i in numbers:
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)