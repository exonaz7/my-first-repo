# Лабораторная работа № 9
# Вариант 3 — класс «Студент»

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        # Добавляем новую оценку в список.
        self.grades.append(grade)

    def average_grade(self):
        # Считаем средний балл с помощью цикла.
        if len(self.grades) == 0:
            return 0

        total = 0
        for grade in self.grades:
            total += grade

        return total / len(self.grades)


def print_student(student):
    # Выводим информацию о студенте.
    print(f"Студент: {student.name}, группа {student.group}")
    print(f"Оценки: {student.grades}")
    print(f"Средний балл: {student.average_grade():.1f}")


def is_good_student(student):
    # Хороший студент имеет средний балл 4 или выше.
    return student.average_grade() >= 4


# Главная часть программы.
st = Student("Бугаев Тимофей Игоревич", "ИИ 13/9")
st.add_grade(5)
st.add_grade(4)
st.add_grade(5)

print_student(st)
print("Отличник:", is_good_student(st))
