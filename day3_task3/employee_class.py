class Employee:
    company_name = None #static variable
    company_location = None

    def __init__(self):
        self.emp_id = None
        self.emp_name = None
        self.emp_salary = None
        self.emp_grade = None

    @staticmethod
    def author_name():
        print("Author is Pratik")

    def print_details_nonstatic(self):
        print(30 * '-')
        print("EMp name", self.emp_name)  # Dynamic variable call with object name and here self is the object
        print("Emp Id", self.emp_id)  # Dynamic variable call with object name and here self is the object
        print("Emp salary", self.emp_salary)  # Dynamic variable call with object name and here self is the object
        print("Emp grade", self.emp_grade)
        print("Compny name", Employee.company_name)  # STatic variable call with class name
        print("Company location", Employee.company_location)  # STatic variable call with class name
        print(30 * '-')

    def count_emp_details(self):
        # self.print_details_nonstatic()
        if self.emp_grade == 'A':
            print(self.emp_name)
            print("10% increment", self.emp_salary * 10 / 100)
        elif self.emp_grade == 'B':
            print(self.emp_name)
            print("15% increment", self.emp_salary * 15 / 100)
        elif self.emp_grade == 'C':
            print(self.emp_name)
            print("5% increment", self.emp_salary * 5 / 100)
        else:
            print(self.emp_name, "No bonus")