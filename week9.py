class Student:
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks

    def calculate_average(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]
        average = total / len(self.marks)
        return average

    def display_average(self):
        print(self.calculate_average())


if __name__ == '__main__':
    student1 = Student(1111, {'CSF': 75, 'FunPro': 80, 'WT': 85})
    student2 = Student(2222, {'CSF': 65, 'FunPro': 70, 'WT': 75})
    student1.display_average()
    student2.display_average()
    print('test')
