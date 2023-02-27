from day3_task3.student_class import Student

std1=Student(1001, "jack", "jack@gmail.com", "45.2")
std2=Student(std_rollno=1002, std_name="peter", std_mailid="peter@gmail.com", std_percent="85.2")
std3=Student(1003, "mark", "mark@gmail.com", "56.5")
std4=Student(1004)
std5=Student(1005, std_name="pratik", std_percent=100)

print(std3.get_student_name)

print(std5.print_name_with_percent)