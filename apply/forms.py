from django import forms

from .models import Qualification, Student


class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100)
    email = forms.EmailField()

class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)


class StudentForm(forms.ModelForm):
    surname = forms.CharField(max_length=200)

    class Meta:
        model = Student
        fields = ['surname','surname','full_names','date_of_birth','gender','citizenship','identity_number','passport_number','cell_number',
                  'email_address','telephone','address','Suburb','City','postal_code','name_and_surname',
                  'work_number']
        widgets = {
            'surname':forms.TextInput(attrs={"placeholder":'Your Last Name','class':"mn"})

        }


class QualificationForm(forms.ModelForm):
    SHORT_COURSES_CHOICES = (
        ('Short Course 1', 'Short Course 1'),
        ('Short Course 2', 'Short Course 2'),

    )
    FET_CERTIFICATE_CHOICES = (
        ('Systems Development', 'Systems Development'),
        ('Advertising', 'Advertising'),
        ('Technical Support', 'Technical Support'),

    )
    NATIONAL_CERTIFICATE_CHOICES = (
        ('Advertising', 'Advertising'),
        ('Business Analysis', 'Business Analysis'),
        ('Systems Development', 'Systems Development'),
        ('Business Analysis Support Practises', 'Business Analysis Support Practises'),
        ('End User Computing', 'End User Computing'),
        ('System Support', 'System Support'),

    )
    apply_for_academy_year = forms.SelectDateWidget()
    programe_type = forms.Select(choices=SHORT_COURSES_CHOICES)
    highest_grade_passed = forms.CharField(max_length=200)
    name_of_high_school = forms.CharField(max_length=200)
    final_examination_date = forms.SelectDateWidget(years=None)
    certified_identity_document = forms.FileField()
    certified_metric_certificate = forms.FileField()

    class Meta:
        model = Qualification
        fields = ['apply_for_academy_year', 'programe_type', 'highest_grade_passed', 'name_of_high_school',
                  'final_examination_date', 'certified_identity_document', 'certified_metric_certificate']
