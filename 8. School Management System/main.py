from school import School
from person import Person, Teacher, Student
from subject import Subject
from classroom import Classroom

School=School('DIU', 'Badda, Dhaka')

eight=Classroom('Eight')
nine=Classroom('Nine')
ten=Classroom('Ten')

#adding class romm
School.add_classroom(eight)
School.add_classroom(nine)
School.add_classroom(ten)

#adding student
rahim= Student('Rahim',eight)
karim= Student('Karim',nine)
fahim= Student('Fahim',ten)
hamim= Student('Hamim',ten)

School.student_admission(rahim)
School.student_admission(karim)
School.student_admission(fahim)
School.student_admission(hamim)

#adding teachers
abul=Teacher('Abul Khan')
babul=Teacher('Babul Khan')
kabul=Teacher('Kbul Khan')

#adding Subjects
bangla=Subject('Bangla', abul)
physics=Subject('Physics', babul)
chemistry=Subject('Chemistry', kabul)
biology=Subject('Biology', kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

print(School)