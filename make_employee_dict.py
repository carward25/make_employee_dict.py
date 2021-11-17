#name: Cassidy Ward
#date: 11/17/2021
#description: this program serves as a dictionary for storing employee names, salaries, ID number, and email.



class Employee:


    def __init__(self, name, ID_number, salary, email):

        #Set the values of the data members of the class.

        self.name = name

        self.ID_number = ID_number

        self.salary = salary

        self.email_address = email

def make_employee_dict(list_names, list_ID, list_salary, list_email):

    employee_dict = {}

    list_len = len(list_ID)

    for i in range(list_len):

        name = list_names[i]

        id_num = list_ID[i]

        salary = list_salary[i]

        email = list_email[i]

        employee_dict[id_num] = Employee(name, id_num, salary, email)

    return employee_dict