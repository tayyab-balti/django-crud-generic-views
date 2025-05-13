from django.shortcuts import render
from .models import Student
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'roll_no']
    template_name = 'myapp/student_form.html'
    success_url = '/students/'

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'myapp/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'myapp/student_detail.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'roll_no']
    success_url = '/students/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    context_object_name = 'student'
    success_url = '/students/'