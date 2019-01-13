count = 0
count = count + 1
print(count)

count += 1
print(count)

count = 7 // 3
print(count)

count = 7 % 3
print(count)

numbers = [i for i in range(1, 8)]
print(numbers)
for number in numbers:
    if number % 2 == 1:
        print(number, ': 홀수')
    else:
        print(number, ': 짝수')

print(not False)
print(True and False)
print(True or False)

fruits = ['사과', '딸기', '망고', '브로콜리', '바나나']
print(fruits)
print('딸기' in fruits)
print('땅기' not in fruits)

if fruits[1] == '딸':
    print("Yes")
    print("딸기")
else:
    print("No")
    print("아니래")

count = 0
while count < 1000:
    count += 1
    if count < 4:
        continue
    if count == 8:
        break
    print('횟수: ', count)
