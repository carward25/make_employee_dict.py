#name: Cassidy Ward
#date: 11/17/2021
#description: this program serves as a dictionary for storing employee names, salaries, ID number, and email.

#Define the class Employee.

class Employee():
    def __init__(self, name, Id, sal, email):
        self.employee_name = name
        self.ID_number = Id
        self.salary = sal
        self.email_address = email


def make_employee_dict(names, ids, salaries, emails):
    employee_dict = {}

    for i in range(len(names)):
        emp = Employee(names[i], ids[i], salaries[i], emails[i])
        employee_dict[ids[i]] = emp
    return employee_dict


def main():
    names = ['John', 'Peter', 'Marsha', 'Jason']
    ids = [1, 2, 3, 4]
    salaries = [1200, 1300, 1400, 1500]
    emails=['john@email.com','peter@email.com','marsha@email.com','jason@email.com']

    emp_dict = make_employee_dict(names,ids,salaries,emails)
    print(emp_dict)


main()