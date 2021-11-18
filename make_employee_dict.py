#name: Cassidy Ward
#date: 11/17/2021
#description: this program serves as a dictionary for storing employee names, salaries,
# ID number, and email.


class Employee:
    def __init__(self, name, ID, salary, email):
        self.__name = name
        self.__ID = ID
        self.__salary = salary
        self.__email = email

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email

def make_employee_dict(names, ids, salaries, emails):
    employee_dict = dict()
    for i in range(len(names)):
        employee = Employee(names[i], ids[i], salaries[i], emails[i])
        employee_dict[ids[i]] = employee
    return employee_dict


if __name__ == '__main__':
    emp_names = ["Jean", "Kat", "Pomona"]
    emp_ids = ["100", "101", "102"]
    emp_sals = [30, 35, 28]
    emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
    result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
    print(result["100"].get_name())
