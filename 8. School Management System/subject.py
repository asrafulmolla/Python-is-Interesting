from person import Teacher
from school import School

class Subject:
    def __init__(self, name, teacher):
        self.name=name
        self.teacher=teacher #teacher object thakbe
        self.mmax_marks=100
        self.pass_marks=33
    def exam(self, students): #students list
        for student in students:
            mark=self.teacher.evaluate_exam() #randomly mark
            student.marks[self.name]=mark
            student.subject_grade[self.name]=School.claculate_grade(mark)
            