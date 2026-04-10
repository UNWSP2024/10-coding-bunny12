# Author: Abrielle Nyei
# Date: 2026-04-09
# Title: Employee Class Program

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        print("Name:", self.name)
        print("ID Number:", self.id_number)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("-" * 30)


def main():
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    print("Employee Information:\n")
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()


if __name__ == "__main__":
    main()