
# הגדרת פונקציית למדא לממוצע של שלושה מספרים
avg3 = lambda a, b, c: (a + b + c) / 3

# קריאה לפונקציה והדפסת התוצאה
result = avg3(10, 4, 7)
print(result)  # 7.0


# יצירת רשימה של רשומות (מחרוזת, מספר)
records = [("banana", 3), ("apple", 5), ("date", 2), ("fig", 7), ("cherry", 1)]

sorted_by_str = sorted(records, key=lambda t: t[0])
print(sorted_by_str)
# [('apple', 5), ('banana', 3), ('cherry', 1), ('date', 2), ('fig', 7)]


sorted_by_num = sorted(records, key=lambda t: t[1])
print(sorted_by_num)
# [('cherry', 1), ('date', 2), ('banana', 3), ('apple', 5), ('fig', 7)]




students = [
    {"name": "Noa",  "age": 22, "grade": 88},
    {"name": "Avi",  "age": 24, "grade": 95},
    {"name": "Dana", "age": 21, "grade": 88},
    {"name": "Leeya","age": 23, "grade": 72},
]



sorted_by_age = sorted(students, key=lambda s: s["age"])
print(sorted_by_age)
# [{'name': 'Dana', 'age': 21, 'grade': 88},
#  {'name': 'Noa',  'age': 22, 'grade': 88},
#  {'name': 'Leeya','age': 23, 'grade': 72},
#  {'name': 'Avi',  'age': 24, 'grade': 95}]



sorted_by_grade_desc = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_by_grade_desc)
# [{'name': 'Avi',  'age': 24, 'grade': 95},
#  {'name': 'Noa',  'age': 22, 'grade': 88},
#  {'name': 'Dana', 'age': 21, 'grade': 88},
#  {'name': 'Leeya','age': 23, 'grade': 72}]

