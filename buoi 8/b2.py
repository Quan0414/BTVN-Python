class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def describe(self):
        pass

    def get_age(self, current_year=2024):
        return current_year - self.yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people = []

    def addPerson(self, person: Person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def countDoctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sortAge(self):
        self.people.sort(key=lambda person: person.get_age())

    def aveTeacherYearOfBirth(self):
        teachers = [person.yob for person in self.people if isinstance(person, Teacher)]
        return sum(teachers) / len(teachers) if teachers else 0
