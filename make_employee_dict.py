#name: Cassidy Ward
#date: 11/17/2021
#description: this program serves as a dictionary for storing employee names, salaries, ID number, and email.

#Define the class Employee.

class Employee:
    def __init__(self, name, ID_number, salary, email):
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

def main():

    sample_names = ["NAME 1", "NAME 2", "NAME 3", "NAME 4"]
    sample_ids = ["ID1", "ID2", "ID3", "ID4"]
    sample_salaries = [1000, 2000, 3000, 4000]
    sample_emails = ["abc@xyz.com", "xyz@abc.com", "sample@sample.com", "aaa@bbb.com"]
    result = (make_employee_dict(sample_names, sample_ids, sample_salaries, sample_emails))

    for i in result:


        print(i+": ")
        print("Name:", result[i].name)
        print("ID NUMBER:", result[i].ID_number)
        print("SALARY:", result[i].salary)
        print("EMAIL:", result[i].email_address)
        print()
main()