from day3_task3.employee_class import Employee

Employee.company_name = "eInfochips"
Employee.company_location = 'Ahmedabad,Gujarat'
print(Employee.company_name+Employee.company_location)

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.emp_id=11
emp1.emp_name='Paul'
emp1.emp_salary=500
emp1.emp_grade='A'

emp2.emp_id=10
emp2.emp_name='kim'
emp2.emp_salary=900
emp2.emp_grade='B'

emp3.emp_id=13
emp3.emp_name='Jazz'
emp3.emp_salary=800
emp3.emp_grade='C'

print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)

Employee.author_name()


emp1.print_details_nonstatic()
emp2.print_details_nonstatic()
emp3.print_details_nonstatic()

print("Count details")
emp1.count_emp_details()
emp2.count_emp_details()
emp3.count_emp_details()