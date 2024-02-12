class Student:
    def __init__(self, name, section, rolln, dept='CSE'):
        self.name = name
        self.section = section
        self.rolln = rolln
        self.dept = dept

    def display_student(self):
        print(f'''Name: {self.name}
Section: {self.section}
Roll no.: {self.rolln}
Department: {self.dept}''')
        
st1=Student("Vivek", 'CB', 62)
st2=Student("Rakshit", 'CB', 40)
st3=Student("Kamal", 'CB', 22)

st1.display_student()
st2.display_student()
st3.display_student()