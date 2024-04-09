from django.shortcuts import render, redirect

from term_app.forms import employee_form
from term_app.models import employee


# Create your views here.
def index(request):
    return render(request, "welcome.html")
# def homepage(request):
#     return render(request, "welcome.html")

def about(request):
    return render(request, "new.html")
def add_employee(request):
    form = employee_form()
    if request.method == 'POST':
        obj = employee_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("view")
    return render(request, 'view_employee.html', {'form': form})

def view(request):
    data = employee.objects.all()
    return render(request, "new_employee.html", {'new': data})

def delete_data(request,id):
    data = employee.objects.get(id=id)
    data.delete()
    return redirect("view")

def update_data(request,id):
    data = employee.objects.get(id=id)
    form = employee_form(instance=data)
    if request.method == 'POST':
        form = employee_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view")
    return render(request,'update_data.html',{'form':form})
