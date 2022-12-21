from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Course name')
    month_to_learn = models.IntegerField(verbose_name='Month')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name.islower():
            self.name.title()
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    email = models.EmailField(verbose_name='Email',unique=True)
    phone_number = models.CharField(max_length=20,verbose_name='Phone number')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.phone_number.startswith('0'):
            self.phone_number.replace('0','+996',1)
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    class Os(models.TextChoices):
        Win = "1", "windows"
        Mac = "2", "mac"
        Lin = "3", "linux"
    work_study_place = models.CharField(max_length=255,null=True)
    has_own_notebook = models.BooleanField(default=False)
    preferred_os = models.CharField(max_length=2, choices=Os.choices, default=Os.Win)

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=30,verbose_name="Main work",null=True)
    experience = models.DateField(verbose_name='Experience')
    courses = models.ManyToManyField(Student, related_name='mentors', through='Course' )

    def __str__(self):
        return f'{self.main_work} - {self.experience}'


class Course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name='Course name')
    course_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField(verbose_name='Date started')
    course_mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    course_student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def get_end_date(self):
        return self.course_language.month_learn + self.date_started.month


