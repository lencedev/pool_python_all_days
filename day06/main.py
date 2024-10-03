# task 1.1

# Can you explain this piece of code?
# def f(x) :
#     return 2 * x + 1

# def g():
#     return 7

# y = f(2)
# print(y)
# y = f(5) + g()
# print(y)

# task 1.2

# def bread() :
#     print(" <////////// > " )
# def lettuce() :
#     print(" ~~~~~~~~~~~~ " )
# def tomato() :
#     print(" O O O O O O " )
# def ham() :
#     print(" ============ " )

# bread()
# lettuce()
# tomato()
# ham()
# bread()

# task 1.3

# def bread() :
#     print(" <////////// > " )
# def lettuce() :
#     print(" ~~~~~~~~~~~~ " )
# def tomato() :
#     print(" O O O O O O " )
# def ham() :
#     print(" ============ " )

# for i in range(0,41):
#     bread()
#     lettuce()
#     tomato()
#     ham()
#     bread()

# task 1.4

# def bread() :
#     print(" <////////// > " )
# def lettuce() :
#     print(" ~~~~~~~~~~~~ " )
# def tomato() :
#     print(" O O O O O O " )
# def ham() :
#     print(" ============ " )

# def making_sandwich():
#     x = input("how many sandwich u want? \n")
#     for i in range(int(x)):
#         bread()
#         lettuce()
#         tomato()
#         ham()
#         bread()
#         print("\n")
#     return

# making_sandwich()

# task 1.5

# def bread() :
#     print(" <////////// > " )
# def lettuce() :
#     print(" ~~~~~~~~~~~~ " )
# def tomato() :
#     print(" O O O O O O " )
# def ham() :
#     print(" ============ " )

# def make_hamburger():
#         bread()
#         lettuce()
#         tomato()
#         ham()
#         bread()

# def make_veg():
#         bread()
#         for i in range(0, 2):
#             lettuce()
#             tomato()
#         bread()

# def making_sandwich():
#     x = input("how many sandwich u want? \n")
#     veg = input("are you veg ? if yes type 1 else type w/e \n")
#     for i in range(int(x)):
#         if veg == "yes":
#             make_veg()
#         else:
#             make_hamburger()
#         print("\n")
#     return
# making_sandwich()

# CHALLENGE

# import time

# def fast_exponentiation(base, exp):
#     if exp == 0:
#         return 1
#     elif exp % 2 == 0:
#         half_power = fast_exponentiation(base, exp // 2)
#         return half_power * half_power
#     else:
#         return base * fast_exponentiation(base, exp - 1)


# def expo():
#     start_time = time.time()
#     result = fast_exponentiation(3, 4)
#     end_time = time.time()
#     print(result)
#     print(f"Time taken: {end_time - start_time} seconds")
# expo()

# task 2.1

# import string
# import re

# def epitech_mdr(input_text):
#     if input_text == '':
#         return ''
#     print(string.punctuation)
#     if input_text[0].count(string.punctuation) > 0:
#         return epitech_mdr(input_text[1:])
#     return input_text[0] + epitech_mdr(input_text[1:])

# def remove_punctuation(input_text):
#     return re.sub(r'[^\w]', '', input_text).lower()

# def is_palindrome():
#     print(epitech_mdr("abc@!qs dzeju"))
#     mystr = remove_punctuation(input("give me a texte : \n"))
#     print(mystr)
#     reversed_str = mystr[::-1]

#     if reversed_str != mystr:
#         return(print("not a palindrome"))
# is_palindrome()

# task 2.2
# import os

# def explore_directory(path, level=0):
#     base_lvl = 0
#     os.chdir(path)
#     print(' ' * level + os.path.basename(path))
#     items = os.listdir()
#     has_directory = False

#     for item in items:
#         if os.path.isdir(item):
#             has_directory = True
#             new_path = os.path.join(os.getcwd(), item)
#             explore_directory(new_path, level + 1)
#         else:
#             print(' ' * (level + 1) + item)
#     os.chdir('..')

# start_path = os.getcwd()
# explore_directory(start_path)

# task 3.1

# import string

# def funA(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.islower()) == nb else 0
# def funB(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isupper()) == nb else 0
# def funC(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isalpha()) == nb else 0
# def funD(mystr, nb):
#     return 1 if sum(1 for char in mystr if char in string.punctuation) == nb else 0
# def funE(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isnumeric()) == nb else 0



# task 3.2

# import string

# def lower(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.islower()) >= nb else (print(f"The string has fewer than {nb} lowercase characters.") or 0)
# def upper(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isupper()) >= nb else (print(f"The string has fewer than {nb} uppercase characters.") or 0)
# def alpha(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isalpha()) >= nb else (print(f"The string has fewer than {nb} characters.") or 0)
# def special(mystr, nb):
#     return 1 if sum(1 for char in mystr if char in string.punctuation) >= nb else (print(f"The string has fewer than {nb} punctuation characters.") or 0)
# def numeric(mystr, nb):
#     return 1 if sum(1 for c in mystr if c.isnumeric()) >= nb else (print(f"The string has fewer than {nb} numerics characters.") or 0)


# def checkpassword(option, nb, password):
#     print(option(password, nb))

# checkpassword(lower, 4, "Ooooo") or checkpassword(special, 4, "mys!!ecr!!assword")

# check_password(lower ,4 , "mysecretpassword" )
# check_password(special , 2 , "mysecretpassword " )


