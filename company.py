#from employee is the file name and import Employee is the class name in employee that we defined
from employee import Employee

class Company: 
    def __init__(self):
        self.employees = []
    
    def add_employees(self, new_employee):
        self.employees.append(new_employee)

def main():
    my_company = Company()

    employee1 = Employee('Justine', 'Cacho', 50000)
    my_company.add_employee(employee1)
    employee2 = Employee('Travis', 'Scott', 25000)
    my_company.add_employee(employee2)
    employee3 = Employee('Justine', 'Cacho', 60000)
    my_company.add_employee(employee3)

    print(my_company.employees)
    