"""
Scenario:
Hifz class has 5 new students this year. Store each student's name, age, and their current Surah in a dictionary.
Put all 5 dictionaries in a list.
Then use a for loop to print each student's full info nicely.
"""


student_1 = {
    "name": "Ali",
    "age": 10,
    "surah": "Al-Fatiha"
}
student_2 = {
    "name": "Ahmed",
    "age": 12,
    "surah": "Al-Baqarah"
}
student_3 = {
    "name": "Yousuf",
    "age": 11,
    "surah": "Al-Imran"
}
student_4 = {
    "name": "Omar",
    "age": 13,
    "surah": "An-Nisa"
}
student_5 = {
    "name": "Osman",
    "age": 9,
    "surah": "Al-Ma'idah"
}


students = [student_1, student_2, student_3, student_4, student_5]

# print(student_1["name"])
# print(student_2["name"])
# print(student_3["name"])
# print(student_4["name"])
# print(student_5["name"])

# for i in students:
#     print(i["name"])

for i in students:
    print("Name:", i["name"], " | ", "Age:", i["age"], " | ", "Surah:", i["surah"])
