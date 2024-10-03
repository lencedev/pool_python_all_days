# task 1.1

# def my_list():
#     lst = [0, 1, 2, 3, 4]
#     print(lst[0])
# my_list()

# task 1.2

# def my_list():
#     lst = [0, 1, 2, 3, 4]
#     print(lst[-1])
# my_list()


# task 1.3

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     lst.append(6)
#     print(lst)
# my_list()

# task 1.4

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     print(lst)
# my_list()

# task 1.5

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     print(lst)
#     lst = lst[:-1]
#     print(lst)
# my_list()

# task 1.6

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     print(lst)
#     lst.insert(0, 9)
#     print(lst)
# my_list()

# task 1.7

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     print(lst[1:5])
# my_list()

# task 1.8

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     new_lst= lst[::-1]
#     print(new_lst)
# my_list()

# task 1.9

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]
#     print(lst[::2])
# my_list()

# task 1.10

# def my_list():
#     lst = [0, 1, 2, 3, 4, 5]

#     for i in range(0, 17):
#         lst.append(i)
#     print(lst)
# my_list()

# task 1.11

# def my_list():
#     # lst = [0, 1, 2, 3, 4, 5]
#     # new_lst = lst[::-1]
#     # lst.extend(new_lst)
#     # print(lst)
#     my_first_list = [7 , 8 , 9]
#     my_second_list = [4 , 5 , 6]
#     my_first_list = [*my_first_list ,*my_second_list ]
#     print(my_first_list)
# my_list()

# task 2.1

# def my_list():
#     lst = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
#     new_lst = 1
#     for i in lst:
#         new_lst *= lst[i]
#     print(new_lst)
# my_list()

# task 2.2
# print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

# task 2.3 & 2.4
# array_list = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
# print(max(array_list))

# task 2.5
# array_list = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
# filtered_list = filter(lambda x: x < 7, array_list)
# print(list(filtered_list))

# array_list = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
# n = len(array_list)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if array_list[j] > array_list[j+1]:
#             array_list[j], array_list[j+1] = array_list[j+1], array_list[j]
#     print(array_list)


# filtered_list = filter(lambda x: x < 7, array_list)


# map(lambda x : x + x, array_list)

# task 2.6

# array_list = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
# n = len(array_list)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if array_list[j] > array_list[j+1]:
#             array_list[j], array_list[j+1] = array_list[j+1], array_list[j]
#     print(array_list[::-1])

# task 2.7

# lst = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
# print(lst)
# if x is even do this, if not do this


# task 2.8
# print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
# if x is true, we keep if not we dont

# task 2.9
# lst = [*enumerate([42, 3, 4, 18, 3, 10])]
# print(lst)
# it enumerate the list with the index and the element

# task 2.10
# first_name = [" Jackie " , " Bruce " , " Arnold " , " Sylvester " ]
# last_name = [" Stallone " , " Schwarzenegger " , " Willis " , " Chan " ]
# magic = [* zip(first_name , last_name[::-1])]
# print(magic[0])
# print(magic[3])
# print(magic[1][0])
# print(magic[0][1])
# print(magic[2])


# import time
# import random

# array_list = [random.randint(1, 1000) for _ in range(1000000)]

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quicksort(left) + middle + quicksort(right)

# startingTime = time.time()
# sorted_list = quicksort(array_list)
# duration = time.time() - startingTime

# print("Temps écoulé pour trier 1 000 000 de nombres avec QuickSort :", duration, "secondes")


# task 3.1

# student = {"name":"owen", "academic year":2027}
# print(student)

# task 3.2

# student = {"name":"owen", "academic year":2027,
#            "units": [
#                {
#                    "name": "Java",
#                    "credits": 4,
#                    "grade" : "B",
#                }
#            ]
#            }
# print(student)

# task 3.3

# grade_weight_mapping = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "E" : 0}

# student = {"name":"owen", "academic year":2027,"total_credits" : 0 ,
#            "units": [
#                {
#                    "name": "Java",
#                    "credits": 3,
#                    "grade" : "B",
#                },{
#                    "name": "Web Development",
#                    "credits": 4,
#                    "grade" : "A",
#                },{
#                    "name": "Network and System Administration",
#                    "credits": 2,
#                    "grade" : "C",
#                },
#            ]
#            }
# total_credits = sum(unit["credits"] for unit in student["units"])
# print(total_credits)
# student["total_credits"] = total_credits
# gpa = student["total_credits"] / len(student["units"])
# print(gpa)

# task 3.4

# grade_weight_mapping = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "E" : 0}

# student1 = {
#     "name": "owen",
#     "academic_year": 2027,
#     "total_credits": 9,
#     "GPA": 3.11,
#     "units": [
#         {"name": "Java", "credits": 3, "grade": "B"},
#         {"name": "Web Development", "credits": 4, "grade": "A"},
#         {"name": "Network and System Administration", "credits": 2, "grade": "C"}
#     ]
# }
# student2 = {
#     "name": "alice",
#     "academic_year": 2026,
#     "total_credits": 8,
#     "GPA": 3.25,
#     "units": [
#         {"name": "Python", "credits": 3, "grade": "A"},
#         {"name": "Networks", "credits": 3, "grade": "B"},
#         {"name": "Data Structures", "credits": 2, "grade": "B"}
#     ]
# }
# student3 = {
#     "name": "john",
#     "academic_year": 2025,
#     "total_credits": 10,
#     "GPA": 2.80,
#     "units": [
#         {"name": "Machine Learning", "credits": 4, "grade": "C"},
#         {"name": "Algorithms", "credits": 3, "grade": "B"},
#         {"name": "Databases", "credits": 3, "grade": "B"}
#     ]
# }
# students = [student1, student2, student3]
# students.sort(key=lambda x: x["GPA"], reverse=True)
# print(students)

# task 4.1


# lst = ["owen", "andrea", "hippo", "nils"]

# def guest_name():
#     mystr = input("Enter a name : ")
#     if mystr in lst:
#         print(mystr)
# guest_name()

# task 4.2

# lst = ["owen", "andrea", "hippo", "nils", "owen"]

# new_lst = []
# def guest_name():
#     for item in lst:
#         if item not in new_lst:
#             new_lst.append(item)
#     print(new_lst)
# guest_name()


# task 4.3



# meetings = [
#     ["Monday", "3:30 PM", "Joe", "Samantha"],
#     ["Tuesday", "4:30 PM", "Ruben", "Samantha"],
#     ["Wednesday", "6:30 PM", "Joe", "Dylan"],
#     ["Thursday", "7:30 PM", "Tim", "Owen"],
#     ["Friday", "8:30 PM", "Gordon", "Nick"],
# ]

# name = input("name : ")
# for item in meetings:
#     if name in item:
#         print(item)

# task 4.4