from django.shortcuts import render
from .models import Employees, Reviews

def index(requests):

    data = Employees.objects.all()
    data2 = Reviews.objects.all()
    context = {
        'data':data,
        'data2': data2
    }
    return render(requests,
                  template_name='index.html',
                  context=context,)

def gallery(requests):
    return render(requests,
                  template_name='gallery.html')

def basic_grid(request):
    return render(request,
                  template_name='basic-grid.html')

def font_icons(request):
    return render(request,
                  template_name='font-icons.html')

def full_width(reguests):
    return render(reguests,
                  template_name='full-width.html')

def sidebar_right(reguests):
    return render(reguests,
                  template_name='sidebar-right.html')

def sidebar_left(reguests):
    return render(reguests,
                  template_name='sidebar-left.html')


