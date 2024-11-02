class StudySubject:
    def __init__(self):
        self.name = input("Введіть назву предмету: ")
        self.hours = int(input(f"Введіть кількість годин для предмету '{self.name}': "))
        self.enable = input(f"Чи доступний предмет '{self.name}' (введіть True або False): ").strip().lower() == 'true'

    def info_study(self):
        print(f"Предмет: {self.name} | Годин: {self.hours} | Доступний: {'Так' if self.enable else 'Ні'}")


class Student:
    def __init__(self):
        self.name = input("Введіть ім'я студента: ")
        self.surname = input("Введіть прізвище студента: ")
        self.study_subjects = self.add_subjects()

    def add_subjects(self):
        subjects = []
        while True:
            add_subject = input("Додати предмет? (введіть 'так' або 'ні'): ").strip().lower()
            if add_subject == 'так':
                subjects.append(StudySubject())
            else:
                break
        return subjects

    def info_student(self):
        print(f"Студент: {self.name} | Прізвище: {self.surname}")

    def info_all(self):
        self.info_student()
        print("Список предметів:")
        for subject in self.study_subjects:
            subject.info_study()


class Group:
    def __init__(self):
        self.group_name = input("Введіть назву групи: ")
        self.age_category = input("Введіть вікову категорію групи: ")
        self.students = self.add_students()
        self.student_count = len(self.students)

    def add_students(self):
        students = []
        while True:
            add_student = input("Додати студента? (введіть 'так' або 'ні'): ").strip().lower()
            if add_student == 'так':
                students.append(Student())
            else:
                break
        return students

    def info_group(self):
        print(f"\nГрупа: {self.group_name} | Вікова категорія: {self.age_category} | Кількість студентів: {self.student_count}")
        print("Інформація про студентів:")
        for student in self.students:
            student.info_all()



group = Group()
group.info_group()
