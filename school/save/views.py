from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from .models import User, Student
from .forms import UserForm, StudentForm


# Create your views here.


# Main view when enter de MyCash Web Page
class IndexView(View):
    def get(self, request):
        return render(request, 'save/index.html')


# Create Object User to Save in DataBase
class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'save/sign_up.html'

    def get_success_url(self):
        return reverse('save:index')


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'save/add_student.html'

    def get_success_url(self):
        return reverse('save:index')
