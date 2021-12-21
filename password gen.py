import random

print('welcome to Your Password Generator')

chars = 'abcdefghjijklmnopqrstuvwxyzABCDEFGNIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number =int(number)

length = input('Password length: ')
length = int(length)

print('\n Here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)