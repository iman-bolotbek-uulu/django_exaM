import datetime
from user.models import Student, Mentor, Language, Course

l1 = Language(name='Python', month_to_learn=6)
l2 = Language(name='JavaScript', month_to_learn=6)
l3 = Language(name='UX-UI', month_to_learn=6)
l1.save()
l2.save()
l3.save()
# test = Language(name='java script', month_to_learn=6)
# test.save()


s1 = Student(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898', work_study_place='School №13', has_own_notebook=True)
s2 = Student(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888', work_study_place='TV', has_own_notebook=True, preferred_os='2')
s3 = Student(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', has_own_notebook=True, preferred_os='3')
s1.save()
s2.save()
s3.save()

m1 = Mentor(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454', main_work=None, experience=datetime.date(year=2021, month=10, day=23))
m2 = Mentor(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876', main_work='University of Fort Collins', experience=datetime.date(year=2010, month=9, day=18))
m1.save()
m2.save()

c1 = Course(course_name='Python', course_language=l1, date_started=datetime.date(year=2022, month=8, day=1), course_mentor=m2, course_student=s1)
c2 = Course(course_name='UXUI', course_language=l3, date_started=datetime.date(year=2022, month=8, day=22), course_mentor=m1, course_student=s3)
c3 = Course(course_name='Python', course_language=l1, date_started=datetime.date(year=2022, month=8, day=1), course_mentor=m2, course_student=s2)
c1.save()
c2.save()
c3.save()


