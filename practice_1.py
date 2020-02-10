# Hello Python Lovers!
'''Welcome
Back'''
print("Hello Python Lovers!")
first_name = 'vasudev'
last_name = 'bonu'

print(last_name.title() + ' ' + first_name.title())
print("{} {}".format(last_name.title(), first_name.title()))
print("{0} {1}".format(last_name.title(), first_name.title()))

name_list = ['bonu', 'vasudev']
print("{0[0]} {0[1]}".format(name_list))

person = {
    'name': 'deva',
    'age': 27
}

sentence = 'My name is {} and I am {} years old.'.format(person['name'].upper(), person['age'])
print(sentence)

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'].upper(), person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

for num in range(11):
    print("The value is {:04}".format(num))

import math
print(math.pi)

pi = 3.14159265
print('Pi value is {:.3f}'.format(pi))

import datetime
date = datetime.datetime(1947,8,15,12)
print(date)
sentence = '{0:%B} {0:%d}th, {0:%Y} is the independance day. {0:%j} th day of that year and that is {0:%A}'.format(date)
print(sentence)

print("{:,.2f}".format(1000000**2))

print("\n")

name = 'vasudeva tirupathi naidu'
print(name)
print(len(name))
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.find('i'))
print(name.find('i', 12, 20))
print(name.count('a'))
print(name.replace('v', 'V'))
print(name.replace('v', 'V', 1))
print(list(name))

list1 = []
for letter in list(name):
    if letter == ' ':
        del letter
    else:
        list1.append(letter)
print(list1)

name = ' vasudev '
print(name=='vasudev')
print(name.strip()=='vasudev')

name = 'vasudeva tirupathi naidu'
print(name.split(' '))
print(''.join(name.split(' ')))
print('-'.join(name))

title = 'INCEPTION'
print(title[::-1])
print(title[1])
print(title.index('I'))
print(title[4:])

print("\n")

num = 3
print(type(num))
num = 3.14
print(type(num))
print(3.14 * 10)
print(0.1 + 0.2)
print(0.1 * 3)
print(first_name, last_name,sep="")
print("{:,.2f}".format(100_000_000_00))
print(f"{10000000000:,.2f}")