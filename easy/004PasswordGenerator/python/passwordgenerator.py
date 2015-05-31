import string
import random


while True:
    no_pass = input("How many passwords to generate: ").split()
    no_char = input("How many characters should each password be: ").split()
    if not len(no_pass) == 1 or len(no_char) == 1:
        print("-- only one input please")
        continue
    try:
        for x in range(int(no_pass[0])):
            pw = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(int(no_char[0]))])
            print(pw)
    except ValueError:
        print("-- numeric input please")
        continue