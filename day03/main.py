# task 1.1

# def print_str():
#     my_str = "test"
#     print(my_str)
# print_str()

# task 1.2

# def print_str():
#     my_str = "abcde"
#     print(my_str[0] + my_str[4])
#     print()
# print_str()

# task 1.3

# def print_str():
#     my_str = "abcde"
#     print(my_str[-1])
#     print()
# print_str()

# task 1.4

# def print_str():
#     my_str = "123456789"
#     print(my_str[3:6])
#     print()
# print_str()

# task 2.1

# def convert_lower_case(mystr):
#     print(mystr.lower())
# convert_lower_case("testLOWERcaseCHAR")

# task 2.2

# def convert_lower_case(mystr):
#     new_sentence = mystr.replace("tu", "ta")
#     print(new_sentence)
# convert_lower_case("tu tu tu tatat")

# task 2.3
# string = "hello world"
# position = string.find("a")
# print(position)
# Return -1 on failure.

# task 2.4

# p = "abcdefghij"
# print(p[::-2][:5][::-1][3:])

# tast 2.5

# p = "abcdefghij"
# print(p[7:][::2])

# task 2.6

# def print_10_times(mystr):
#     i = 0
#     for i in range(0, 10):
#         print(mystr)
# print_10_times("test")

# task 2.7
# print('\n'.join(['10'] * 10))

# task 2.8

# s1 = "Hello "
# s2 = 42
# concat = s1 + str(s2)
# print(concat)
# add str function to s2

# task 2.9
# string1 = "42 "
# string2 = "is "
# string3 = "the answer"
# concat = string1 + string2 + string3
# print ("The string " + concat + " contain " + str(len(concat)) + " characters ) . " )

# task challenge

# def count_occurrences(mystr):
#     words = ["cat", "garden", "mice"]
#     mystr = mystr.lower()
#     nb = 0
#     for word in words:
#         nb += mystr.count(word)
#         nb += mystr.count(word[::-1])
#     print(nb)
# count_occurrences("thE Cat’s cat micetactic wAS tO surpRISE thE mIce iN tHE gArdeN")

# task 3.1

# def ask_username():
#     name = input("what is your name ? \n")
#     print("hello " + name)
# ask_username()

# task 3.2

# def ask_username():
#     name = input("what is your name ? \n")
#     print("hello " + name[0:].capitalize())
# ask_username()

# task 3.3

# def add_sum():
#     nb = input("give me 2 numbers : \n").split()

#     result = int(nb[0]) + int(nb[1])

#     print(f"The sum of {nb[0]} + {nb[1]} = {result}")
# add_sum()

# task 3.4

# def askNumbers():
#     nb = int(input("give me number \n"))
#     print(type(nb))
# askNumbers()

# task 3.5

# import re

# def askStr():
#     mystr = input("Give me a sentence : \n")
#     result = re.split(r'[.?!]', mystr)
#     i = 0
#     print(result)
#     for word in result:
#         first_word = word
#         array = first_word.split()
#         if array:
#             print(array[0])
# askStr()
# comment ça va ? ok. et toi ? ok ! ok
# This is a test. Is it possible to fly? Good things come to those who never give up.

# task 3.6

import numpy as np

french_common_letters = ['e', 'a', 's', 'i', 'n', 'r', 't', 'o', 'l', 'u']
spanish_common_letters = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'l', 'd', 't']

languages_common_letters = [
    ('French', french_common_letters),
    ('Spanish', spanish_common_letters),
]


french_freq = {'a': 7.636, 'b': 0.901, 'c': 3.260, 'd': 3.669, 'e': 14.715, 'f': 1.066, 'g': 0.866, 'h': 0.937, 'i': 7.529, 'j': 0.813, 'k': 0.074, 'l': 5.456, 'm': 2.968, 'n': 7.095, 'o': 5.796, 'p': 2.521, 'q': 1.362, 'r': 6.693, 's': 7.948, 't': 7.244, 'u': 6.311, 'v': 1.838, 'w': 0.049, 'x': 0.427, 'y': 0.708, 'z': 0.326}
english_freq = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.253, 'k': 1.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.250, 'y': 1.974, 'z': 0.074}
german_freq = {'a': 6.516, 'b': 1.886, 'c': 2.732, 'd': 5.076, 'e': 16.396, 'f': 1.656, 'g': 3.009, 'h': 4.577, 'i': 6.550, 'j': 0.268, 'k': 1.417, 'l': 3.437, 'm': 2.534, 'n': 9.776, 'o': 2.594, 'p': 0.670, 'q': 0.018, 'r': 7.003, 's': 7.270, 't': 6.154, 'u': 4.166, 'v': 0.846, 'w': 1.921, 'x': 0.034, 'y': 0.039, 'z': 1.134}
spanish_freq = {'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692, 'g': 1.768, 'h': 1.973, 'i': 6.247, 'j': 2.493, 'k': 0.026, 'l': 4.967, 'm': 3.157, 'n': 6.712, 'o': 8.683, 'p': 2.510, 'q': 0.877, 'r': 6.871, 's': 7.977, 't': 4.632, 'u': 3.927, 'v': 1.138, 'w': 0.027, 'x': 0.515, 'y': 1.433, 'z': 0.467}
portuguese_freq = {'a': 14.634, 'b': 1.043, 'c': 3.882, 'd': 4.992, 'e': 12.570, 'f': 1.023, 'g': 1.303, 'h': 1.281, 'i': 6.186, 'j': 0.879, 'k': 0.015, 'l': 2.779, 'm': 4.738, 'n': 4.446, 'o': 9.735, 'p': 2.523, 'q': 1.204, 'r': 6.530, 's': 6.805, 't': 4.336, 'u': 3.639, 'v': 1.575, 'w': 0.037, 'x': 0.453, 'y': 0.006, 'z': 0.470}
italian_freq = {'a': 11.745, 'b': 0.927, 'c': 4.501, 'd': 3.736, 'e': 11.792, 'f': 1.153, 'g': 1.644, 'h': 0.136, 'i': 10.143, 'j': 0.011, 'k': 0.009, 'l': 6.510, 'm': 2.512, 'n': 6.883, 'o': 9.832, 'p': 3.056, 'q': 0.505, 'r': 6.367, 's': 4.981, 't': 5.623, 'u': 2.813, 'v': 2.097, 'w': 0.033, 'x': 0.008, 'y': 0.020, 'z': 1.181}

languages_freq = {
    'French': french_freq,
    'English': english_freq,
    'German': german_freq,
    'Spanish': spanish_freq,
    'Portuguese': portuguese_freq,
    'Italian': italian_freq,
}
# def calculate_euclidean_distance(unknown_vector, lang_vector):
#     return np.sqrt(np.sum((unknown_vector - lang_vector) ** 2))

# def langage_definder(array):
#     last_10_elements = array[-10:]
#     new_array = [letter for letter, _ in reversed(last_10_elements)]
#     compare(new_array ,french_common_letters)
#     print(new_array)



# def sort_algo(percentage_list):
#     n = len(percentage_list)
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(n - 1):
#             if percentage_list[i][1] > percentage_list[i+1][1]:
#                 percentage_list[i], percentage_list[i+1] = percentage_list[i+1], percentage_list[i]
#                 sorted = False
#     return percentage_list

# def compare(unknown, language):
#     common_letters = [letter for letter in unknown if letter in language]
#     first_score = len(common_letters)
#     second_score = 0
#     max_score = len(language)

#     for i in range(len(unknown)):
#         if unknown[i] == language[i]:
#             second_score += max_score - i
#     result = first_score + second_score
#     # print(common_letters)
#     print(first_score)
#     print(second_score)
#     return result

# def calculate_frequency(mystr):
#     length = len(mystr)
#     all_freq = {}
#     for i in mystr:
#         if i in all_freq:
#             all_freq[i] += 1
#         else:
#             all_freq[i] = 1
#     percentage = [(letter, (count / length) * 100) for letter, count in all_freq.items()]
#     return percentage


def calculate_euclidean_distance(unknown, language):
    all_letters = set(unknown.keys()).union(set(language.keys()))
    # print(set(unknown.keys()))
    # print("________________________")
    # print(all_letters)
    vec1 = np.array([unknown.get(letter, 0) for letter in all_letters])
    print("________________VEC1________________________________________________")
    print(vec1)
    vec2 = np.array([language.get(letter, 0) for letter in all_letters])
    print("__________________VEC2____________________________________________")
    print(vec2)
    distance = np.sqrt(np.sum((vec1 - vec2) ** 2))
    return distance

def remove_non_letters(mystr):
    result = ''.join([char for char in mystr if char.isalpha()]).lower()
    return result

def calculate_frequency(mystr):
    length = len(mystr)
    all_freq = {}
    for i in mystr:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    percentage_dict = {letter: (count / length) * 100 for letter, count in all_freq.items()}
    return percentage_dict


def language_analyzer():
    mystr = input("I'll try to detect the language you are speaking...\n")
    new_str = remove_non_letters(mystr)
    test_freq = calculate_frequency(new_str)
    distances = {}
    for language, freq in languages_freq.items():
        distance = calculate_euclidean_distance(test_freq, freq)
        distances[language] = distance
        print(f"Distance avec {language}: {distance:.2f}")
    closest_language = min(distances, key=distances.get)
    print(f"Langue probable : {closest_language}")
language_analyzer()

