class Employee:
    def __init__(self, emp_name, emp_id, w_hours):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.w_hours = w_hours
    def display_employee_details(self):
        print(f'''Employee Name: {self.emp_name}
Employee Id: {self.emp_id}
Hours Worked: {self.w_hours}''')
    def calculate_salary(self):
        salary_per_hour = 250
        self.salary = self.w_hours*salary_per_hour
        print(self.salary)

emp1 = Employee('Sanjay', 'abc123', 150)
emp2 = Employee('Nikhil', 'abc257', 180)

emp1.calculate_salary()
emp2.calculate_salary()