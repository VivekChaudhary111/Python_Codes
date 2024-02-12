class Student:
    def __init__(self):
        self.name = 'NA'
        self.age = 'NA'
        self.grade = 'NA'
        self.marks = 'NA'
    def setDetails(self, **info):
        self.name = info.get('name', 'NA')
        self.age = info.get('age', 'NA')
        self.grade = info.get('grade', 'NA')
        self.marks = info.get('marks', 'NA')
        
        if self.marks >= 90:
            self.grade = 'O'
        elif self.marks >= 80:
            self.grade = 'A+'
        elif self.marks >= 70:
            self.grade = 'A'
        elif self.marks >= 60:
            self.grade = 'B+'
        elif self.marks >=50:
            self.grade = 'C'
        elif self.marks >=40:
            self.grade = 'D'
        else:
            self.grade = 'F'
    def getDetails(self):
        return f'\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}\n'
    
# main code
student1 = Student()
student1.setDetails(name = "Vivek", age = 18, marks = 91)
student2 = Student()
student2.setDetails(name = "Rakshit", age = 18, marks =90)
print(student1.getDetails())
print(student2.getDetails())
    