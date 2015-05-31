username = input('what is your username? ')
age = input('what is your age? ')
name = input('what is your name? ')

print('your username is ' + username)
print('your age is ' + age)
print('your name is ' + name)
s = name + ' input.txt'
f = open(s, 'w')
f.write(username + '\n' + age + '\n' + name + '\n')
