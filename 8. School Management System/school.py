class School:
    
    def __init__(self, name, address):
        self.name=name
        self.address=address
        self.teachers={} # {"bangla" : teacher object}
        self.classrooms={} # {'class name':'class object'}
    def add_classroom(self, classroom):
        self.classrooms[classroom.name]=classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject]=teacher 
    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named{className}')
    
    @staticmethod
    def claculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks >= 70 and marks<80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map={
            'A+':5.00,
            'A':4.00,
            'A-':3.50,
            'B':3.00,
            'C':2.00,
            'D':1.00,
            'F':0.00
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value): #gpa convert
        if value >=4.5 and value<=5.00:
            return 'A+'
        elif value >= 3.5 and value <4.50:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'
    # def __repr__(self):
    #     # all classroom
    #     print('--------ALL CLASSROOMS--------')
    #     for key in self.classrooms.keys():
    #         print (key)
    #     # all students
    #     print('--------Students-------')
    #     result=''
    #     for key, value in self.classrooms.items():
    #         result+=f'------{key.upper()} Classroom Students\n'
    #         for student in value.students:
    #             result+=f'{student.name}\n'
    #     print (result)
    #     # all subject
    #     print('------subjects------')
    #     subject=''
    #     for key, value in self.classrooms.items():
    #         subject+=f'------{key.upper()} Classroom Subjects\n'
    #         for sub in value.subjects:
    #             subject+=f'{sub.name}\n'
    #     print (subject)
    #     # all teacher 
    #     print('--------Students-------')
    #     for key, value in self.teachers:
    #         print (f'{key} : {value}')
    #     # all students result
    #     print('----Student Exam Marks-------')
    #     for key,value in self.classrooms.items():
    #         for student in value.students:
    #             for k,i in student.marks.items():
    #                 print(student.name,k,i,student.subject_grade[k])
    #             print(student.final_grade())
    #             print('----student end----')
    #     return ''
    
    def __repr__(self):
    
        result = "\n====================== SCHOOL REPORT ======================\n"
        
        # All classrooms
        result += "\n---------- ALL CLASSROOMS ----------\n"
        for key in self.classrooms.keys():
            result += f"- {key}\n"
        
        # Students
        result += "\n---------- STUDENTS PER CLASSROOM ----------\n"
        for key, value in self.classrooms.items():
            result += f"\nClassroom: {key.upper()}\n"
            if value.students:
                result += "\n".join([f"  - {student.name}" for student in value.students]) + "\n"
            else:
                result += "  No students enrolled.\n"
        
        # Subjects
        result += "\n---------- SUBJECTS PER CLASSROOM ----------\n"
        for key, value in self.classrooms.items():
            result += f"\nClassroom: {key.upper()}\n"
            if value.subjects:
                result += "\n".join([f"  - {sub.name}" for sub in value.subjects]) + "\n"
            else:
                result += "  No subjects assigned.\n"
        
        # Teachers
        result += "\n---------- TEACHERS ----------\n"
        if self.teachers:
            for key, value in self.teachers.items():
                result += f"  - {key}: {value}\n"
        else:
            result += "  No teachers assigned.\n"
        
        # Student exam marks
        result += "\n---------- STUDENT EXAM MARKS ----------\n"
        for key, value in self.classrooms.items():
            result += f"\nClassroom: {key.upper()}\n"
            for student in value.students:
                result += f"\n  Student: {student.name}\n"
                result += "    Exam Results:\n"
                for subject, marks in student.marks.items():
                    grade = student.subject_grade.get(subject, "N/A")
                    result += f"      - Subject: {subject}, Marks: {marks}, Grade: {grade}\n"
                result += f"    Final Grade: {student.final_grade()}\n"
                result += "    --------------------------\n"
        
        result += "\n==========================================================\n"
        return result

