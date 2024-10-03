import sys
import argparse


# task 2.1

# def somme_nombres(n):
#     somme = 0
#     for i in range(1, n + 1):
#         nb = int("1" * i)
#         somme += nb
#     return somme

# for n in range(9, 13):
#     total = somme_nombres(n)
#     print(f"Somme des nombres 1, 11, 111, ..., {'1' * n} : {total}")
#     for puissance in range(2, 8):
#         resultat = total ** puissance
#         print(f"Somme puissance {puissance} : {resultat}")
#     print("-" * 40)

# task 2.2

# result = 17 ** 1024
# print(result)

# task 3.1

# arg = sys.argv

# quotient = int(arg[1]) // int(arg[2])
# retenue = int(arg[1]) % int(arg[2])

# number = int(arg[1]) / int(arg[2])
# print(f"number {number}, quotient :{quotient} retenue : {retenue}")

# task 3.2

# nb = int(arg[1])
# if(nb % 2) == 0:
#     print("number is even")
# else : print("number is odd")

# task 3.3

# str = arg[1]
# sum = 0
# for char in str:
#     sum += int(char)
# print(f" {sum}")

# task 3.4

# str = arg[1]

# for char in str:
#     if char == '.':
#         break
#     print(f"{char}",end='')
# print("")


# task 4.1

# pi_approximation = 0
# i = 0

# while True:
#     term = (-1) ** i / (2 * i + 1)
#     pi_approximation += term
#     pi_value = pi_approximation * 4

#     if round(pi_value, 6) == 3.141592:
#         break
#     i += 1
# print(f"Approximation de Pi après {i + 1} termes : {round(pi_value, 6)}")

# task 4.2
# def pi_approximation(iterations):
#     result = 0
#     for k in reversed(range(1, iterations * 2, 2)):
#         result = (k ** 2) / (6 + result)
#     return 3 + result

# iterations = 1000000
# pi_approx = pi_approximation(iterations)

# print(f"Approximation de pi: {pi_approx:.6f}")


# def parse_arguments_to_int_list(array):
#     int_list = [int(arg) for arg in array]
#     # print(int_list)
#     return int_list

# def sort_algo():
#     arguments = sys.argv[1:]
#     array = parse_arguments_to_int_list(arguments)
#     n = len(array)
#     sorted = False
#     i = 0
#     while not sorted:
#         sorted = True
#         for i in range(n - 1):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#                 sorted = False
#     print(array)

# sort_algo()

# def parse_arguments_to_int_list(array):
#     int_list = [int(arg) for arg in array]
#     # print(int_list)
#     return int_list

# def is_sorted(array):
#     for i in range(len(array)):
#         if array[i] < array[i+1]:

# def sort_algo():
#     arguments = sys.argv[1:]
#     array = parse_arguments_to_int_list(arguments)
#     n = len(array)
#     sorted_array = []
#     i = 0
#     sorted_array[i] = array[i]



#     print(array)
