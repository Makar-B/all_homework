class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Person: {self.name} | {self.surname} | Вік: {self.age}')


class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        super().__init__(name, surname, age)
        self.subject = subject
        self.hours = hours
        self.pensione = self.set_pensione()

    def set_pensione(self):
        return self.age >= 60

    def info_teacher(self):
        print(f'Teacher: {self.subject} | Годин: {self.hours} | Пенсія: {"Так" if self.pensione else "Ні"}')

    def info_all(self):
        self.info_person()
        self.info_teacher()


class Group:
    def __init__(self, group_name: str, age_category: str):
        self.group_name = group_name
        self.age_category = age_category
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    @property
    def student_count(self):
        return len(self.students)

    def info_group(self):
        print(f'Група: {self.group_name} | Вікова категорія: {self.age_category} | Кількість студентів: {self.student_count}')


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, progress: float, group: Group):
        super().__init__(name, surname, age)
        self.progress = progress
        self.group = group
        self.pensione = self.set_pensione()
        group.add_student(self)

    def set_pensione(self):
        return self.age >= 60

    def info_student(self):
        print(f'Student: Успішність: {self.progress} | Група: {self.group.group_name} | Пенсія: {"Так" if self.pensione else "Ні"}')

    def info_all(self):
        self.info_person()
        self.info_student()
        self.group.info_group()


class Worker(Person):
    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        super().__init__(name, surname, age)
        self.position = position
        self.duties = duties
        self.pensione = self.set_pensione()

    def set_pensione(self):
        return self.age >= 60

    def info_worker(self):
        print(f'Worker: Посада: {self.position} | Обов\'язки: {self.duties} | Пенсія: {"Так" if self.pensione else "Ні"}')

    def info_all(self):
        self.info_person()
        self.info_worker()


# Приклад використаня

group = Group(group_name="IT-22", age_category="18-22")

student = Student(name="Іван", surname="Ковальчук", age=21, progress=88.5, group=group)
teacher = Teacher(subject="Математика", hours=30, name="Анна", surname="Мельник", age=45)
worker = Worker(name="Олег", surname="Гончарук", age=62, position="Охоронець", duties="Охорона кампуса")

student.info_all()
print("\n")
teacher.info_all()
print("\n")
worker.info_all()
