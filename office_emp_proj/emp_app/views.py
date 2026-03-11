from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        print("post")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, department_id=department, role_id=role, hire_date=datetime.now())
    else:
        print("get")
    return render(request, 'add_emp.html')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')