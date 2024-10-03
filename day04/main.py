# task 1.1
# ?

# task 1.2

# def is_equal_42():
#     test = input("choose a number : ")
#     if (test == "42"):
#         print("Correct it's equal to 42")
# is_equal_42()

# task 1.3
# def is_odd_or_even():
#     nb = int(input("choose a number "))
#     if(nb % 2) == 0:
#         print("number is even")
#     else : print("number is odd")
# is_odd_or_even()


# task 1.4

# def open_door():
#     mystr = input("say something ")

#     if mystr == "open sesame":
#         print("access granted")
#         return
#     if mystr == "will you open, you goddamn":
#         print("access fucking granted")
#         return
#     print("permission denied")
#     return
# open_door()





# task 1.5

# def task_function():
#     my_str = int(input("say something : "))

#     if my_str == 42:
#         print("OK")
#         return
#     if my_str <= 21:
#         print("OK")
#         return
#     if(my_str) % 2 == 0:
#         print("OK")
#     if(my_str/2 < 21):
#         print("OK")
#     if(my_str) % 2 != 0 & my_str >= 45:
#         print("OK")
#     else:
#         print("you got wrong")
#     return
# task_function()



# Task 1.6

# a = 42
# b = 41
# if a == b:
#     print(" A and B are the sames ")
# if b <= a:
#     print( " B is equal or lower as A ")
# if b != a:
#     print( " B is different from A ")

# task 2.1

# for i in range(1, 1000):
#     print(i)

# task 2.2

# def ask_str():
#     new_str = ""
#     my_str = input("Please enter a string: ")
#     for char in my_str:
#         for i in range (0, 2):
#             new_str += char
#     print(new_str)
# ask_str()

# task 2.3

# def is_divisible():
#     for i in range(1, 100):
#         if i % 7 == 0:
#             print(i)
# is_divisible()

# task 2.4

# def multiples():
#     for i in range(-30, 30):
#         if i % 3 == 0 & i % 5 == 0:
#             print("FizzBuzz")
#         if i % 3 == 0:
#             print("FIZZ")
#         if i % 5 == 0:
#             print("BUZZ")
# multiples()


# task 2.5

# def beer():
#     beers_size = 99

#     while beers_size != 1:
#         print(f"{beers_size}" + " bottles of beer on the wall")
#         beers_size -= 1
#         print("Take one down and pass it around," + f"{beers_size}" + " bottles of beer on the wall.\n")

#     print(f"{beers_size}" + " bottle of beer on the wall")
#     print("Take one down and pass it around, no more bottle of beer on the wall.\n")
#     print("Go to the store and buy some more, 99 bottles of beer on the wall.")
# beer()


# task 2.6

# def display_int():
#     nb = int(input("Give me a number : "))

#     for i in range(2, int(nb // 2) + 1):
#         multiples = []
#         y = i
#         while y < nb:
#             multiples.append(y)
#             y+=i
#         print(f"{multiples[::-1]}")
# display_int()

# CHALLENGE

# def display_str():
#     my_str = input("Give me an integer and a string : ").split()

#     if (int(my_str[0]) == 0):
#         return
#     if (set("aeiou").intersection(my_str[1].lower())):
#         print("VOWEL")
#     if (int(my_str[0]) >= 42):
#         print(my_str[0])
#     else:
#         print(my_str[1])
# display_str()

# task 3.1

# def encrypt():
#     key = int(input("Give a key : "))
#     message = input("Give a message : ")
#     lst = []
#     i = 0
#     for char in message:
#         if char == " ":
#             lst.append(" ")
#             continue
#         if char.islower():
#             new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
#             lst.append(new_char)
#         if char.isupper():
#             new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
#             lst.append(new_char)
#     print("".join(lst))
# encrypt()


# task 3.2

# def decrypt():
#     message = input("Give a message : ")
#     for letter in range(0, 26):
#         lst = []
#         for char in message:
#             if char == " ":
#                 lst.append(" ")
#                 continue
#             if char.islower():
#                 new_char = chr((ord(char) - ord('a') + letter) % 26 + ord('a'))
#                 lst.append(new_char)
#             if char.isupper():
#                 new_char = chr((ord(char) - ord('A') + letter) % 26 + ord('A'))
#                 lst.append(new_char)
#         print("".join(lst) + "\n")
#     return
# decrypt()

# task 3.3

def uncoder():
    text = input("give me the text : ")
    old_key = input("give me the key : ")
    new_key = []
    new_letter = []

    if len(old_key) < len(text):
        for i in range(0, len(text)):
            if text[i] == " ":
                new_key.append(" ")
            new_key.append(old_key[i % len(old_key)])

        for i in range(0, len(text)):
            if text[i].isalpha():
                if text[i].islower():
                    new_char = chr(((ord(text[i]) + ord('a') - (ord(new_key[i]) - ord('a'))) % 26) + ord('a'))
                elif text[i].isupper():
                    new_char = chr(((ord(text[i]) + ord('A') - (ord(new_key[i]) - ord('A'))) % 26) + ord('A'))
                new_letter.append(new_char)
            else:
                new_letter.append(text[i])
        print("".join(new_letter))
    return

def coder():
    text = input("give me the text : ")
    old_key = input("give me the key : ")
    new_key = []
    new_letter = []

    if len(old_key) < len(text):
        for i in range(0, len(text)):
            if text[i] == " ":
                new_key.append(" ")
            new_key.append(old_key[i % len(old_key)])

        for i in range(0, len(text)):
            if text[i].isalpha():
                if text[i].islower():
                    new_char = chr(((ord(text[i]) - ord('a') + (ord(new_key[i]) - ord('a'))) % 26) + ord('a'))
                elif text[i].isupper():
                    new_char = chr(((ord(text[i]) - ord('A') + (ord(new_key[i]) - ord('A'))) % 26) + ord('A'))
                new_letter.append(new_char)
            else:
                new_letter.append(text[i])
        print("".join(new_letter))
    return

def menu():
    my_str = input("Type 1 to enter coder or 2 to decode : ")
    if (my_str == "1"):
        return coder()
    return uncoder()
menu()

# task 3.4

