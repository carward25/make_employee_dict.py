#name: Cassidy Ward
#date: 11/17/2021
#description: this program serves as a dictionary for storing employee names, salaries,
# ID number, and email.
class Employee:

    # Initializing the class variables

    def __init__(self, employee_name, id_number, salary, email_address):
        self.employee_name = employee_name

        self.id_number = id_number

        self.salary = salary

        self.email_address = email_address


# This function creates an dictionary of Employee objects where the key is the employee id and the value is the Employee object

def make_employee_dict(names_lst, id_lst, salary_lst, email_address_lst):
    # This dictionary stores the dictionary of Employee Objects

    employees_dict = {}

    # Iterating over the names, id, salary, email address lists parallelly

    for list_index in range(len(names_lst)):
        # Creating an Employee object

        employee = Employee(names_lst[list_index], id_lst[list_index], salary_lst[list_index],
                            email_address_lst[list_index])

        # Adding the Employee object to the dictionary using id_num as key and object as value

        employees_dict[id_lst[list_index]] = employee

    # Returning the dictionary of Employee objects

    return employees_dict


# This is the main function

def main():
    # This is a list of employee names

    names = ["Russell Norvig", "Jim Kay", "Jimmy Soni", "Rob Goodman"]

    # This is a list of employee id numbers

    ids = [12345, 12332, 34523, 98765]

    # This is a list of employee salaries

    salaries = [12000, 32400, 45000, 87300]

    # This is a list of employee email addresses

    emails = ["russell@outlook.com", "jimkay2@yahoo.com", "jimmy234@outlook.com", "goodmanrob123@outlook.com"]

    # Getting the dictionary of employee objects

    employee_info_dict = make_employee_dict(names, ids, salaries, emails)

    # Printing the data of each employee

    print("Data of employees:\n")

    # Iterating over dictionary

    for employee in employee_info_dict:
        # Getting the Employee object of current employee

        emp_obj = employee_info_dict[employee]

        # Printing data of employee

        print("Name: %s" % emp_obj.employee_name)

        print("ID: %d" % emp_obj.id_number)

        print("Salary: %d" % emp_obj.salary)

        print("Email address: %s\n" % emp_obj.email_address)


# Calling the main function

main()