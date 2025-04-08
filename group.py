from exceptions import GroupFullException

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        if student not in self.group:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student in self.group:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Group number: {self.number}\n{all_students.strip()}'