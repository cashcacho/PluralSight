#Create a class of Employee with an init method to access fname, lname, and salary
class Employee:
    def __init__(self, fname, lname, salary):
        #Initialize the employee properties to those passed-in values
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52