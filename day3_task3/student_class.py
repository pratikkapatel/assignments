class Student:
    sch_name = None
    sch_add = None

    def __init__(self, std_rollno, std_name=None, std_mailid=None, std_percent=None):
        self.std_rollno = std_rollno
        self.std_name = std_name
        self.std_mailid = std_mailid
        self.std_percent = std_percent

    @property
    def get_student_name(self):
        return self.std_name

    @property
    def print_name_with_percent(self):
        return "Hi "+self.std_name+" your percentage is - "+ str(self.std_percent)