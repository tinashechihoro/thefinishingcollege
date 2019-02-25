import os

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from formtools.wizard.views import SessionWizardView

from .forms import QualificationForm, StudentForm, FormStepOne, FormStepTwo
from .models import Student, Qualification


class FormWizardView(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))

    def done(self, form_list, **kwargs):
        for form in form_list:
            form_data = form.cleaned_data
            student = Student()
            qualification = Qualification()
            student.qualification = Qualification()
            student.surname = form_data['surname']
            student.full_names = form_data['full_names']
            student.date_of_birth = form_data['date_of_birth']
            student.gender = form_data['gender']
            student.citizenship = form_data['citizenship']
            student.identity_number = form_data['identity_number']
            student.passport_number = form_data['passport_number']
            student.cell_number = form_data['cell_number']
            student.email_address = form_data['email_address']
            student.telephone = form_data['telephone']
            student.address = form_data['address']
            student.Suburb = form_data['Suburb']
            student.City = form_data['City']
            student.postal_code = form_data['postal_code']
            student.name_and_surname = form_data['name_and_surname']
            student.work_number = form_data['work_number']
            # qualification.apply_for_academy_year = form_data['apply_for_academy_year']
            # qualification.programe_type = form_data['programe_type']
            # qualification.highest_grade_passed = form_data['highest_grade_passed']
            # qualification.name_of_high_school = form_data['name_of_high_school']
            # qualification.final_examination_date = form_data['final_examination_date']
            # qualification.certified_identity_document = form_data['certified_identity_document']

            student.save()
            #qualification.save()


            return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)


def index(request):
    """index page"""
    return render(request, 'application/index.html', {})


def about_us(request):
    """index page"""
    return render(request, 'application/about_us.html', {})


def admissions(request):
    """index page"""
    return render(request, 'application/admissions.html', {})


def contact_us(request):
    """index page"""
    return render(request, 'application/contact_us.html', {})


def apply(request):
    """index page"""
    form = QualificationForm()
    student = StudentForm()
    return render(request, 'application/apply.html', {'form': form, 'student': student})
