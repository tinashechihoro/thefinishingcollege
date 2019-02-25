from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Student Model"""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),

    )
    # application details
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    surname = models.CharField(max_length=200, help_text='Your last name')
    full_names = models.CharField(max_length=200, help_text='Your first name(s)')
    date_of_birth = models.DateTimeField(auto_now_add=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=200, default='south africa')
    identity_number = models.CharField(max_length=25)
    passport_number = models.CharField(max_length=25)

    # contact_details
    cell_number = models.CharField(max_length=50)
    email_address = models.EmailField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, help_text='House No and Street Name')
    Suburb = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)

    # next_of_kin
    name_and_surname = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    cell_number = models.CharField(max_length=50)
    work_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.identity_number, self.passport_number)




class Qualification(models.Model):
    """Qualification model"""
    CHOICES = (

        ('Short Courses', (

            ('Short Course 1', 'Short Course 1'),
            ('Short Course 1', 'Short Course 1'),

        )),

        ('FET Certificate', (

            ('Systems Development', 'Systems Development'),
            ('Advertising', 'Advertising'),
            ('Technical Support', 'Technical Support'),

        )),

        ('NATIONAL Certificate', (

            ('Advertising', 'Advertising'),
            ('Business Analysis', 'Business Analysis'),
            ('Systems Development', 'Systems Development'),
            ('Business Analysis Support Practises', 'Business Analysis Support Practises'),
            ('End User Computing', 'End User Computing'),
            ('System Support', 'System Support'),

        )),

    )


    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    apply_for_academy_year = models.DateField()
    programe_type = models.CharField(choices=CHOICES,max_length=100)

    # Educational Background
    highest_grade_passed = models.CharField(max_length=200)
    name_of_high_school = models.CharField(max_length=200)
    final_examination_date = models.DateField(auto_now_add=False)
    certified_identity_document = models.FileField(upload_to='uploads/')
    certified_metric_certificate = models.FileField(upload_to='uploads/')

    """
    Notes 

    """
