from operator import itemgetter

# פונקציה לחישוב ממוצע של שלושה מספרים
def avg3(a, b, c):
    return (a + b + c) / 3

result = avg3(10, 4, 7)
print(result)  # 7.0


# דוגמה למיון רשימת tuples
records = [("banana", 3), ("apple", 5), ("date", 2), ("fig", 7), ("cherry", 1)]

# מיון לפי המחרוזת
sorted_by_str = sorted(records, key=itemgetter(0))
print(sorted_by_str)

# מיון לפי המספר
sorted_by_num = sorted(records, key=itemgetter(1))
print(sorted_by_num)


# דוגמה למיון רשימת מילונים
students = [
    {"name": "Noa",  "age": 22, "grade": 88},
    {"name": "Avi",  "age": 24, "grade": 95},
    {"name": "Dana", "age": 21, "grade": 88},
    {"name": "Leeya","age": 23, "grade": 72},
]

# מיון לפי גיל
sorted_by_age = sorted(students, key=lambda s: s["age"])
print(sorted_by_age)

# מיון לפי ציון בסדר יורד
sorted_by_grade_desc = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_by_grade_desc)
