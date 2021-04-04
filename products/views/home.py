from django.shortcuts import render
from django.http import HttpResponse
from products.models.slider import Slider
from products.models.departments import Department
from products.models.item import Item
from products.models.contact import Contact
from django.contrib.auth import get_user_model


def index(request):
    sliders = Slider.objects.filter(active=1)
    depatments = Department.objects.filter(active=1)
    all_items = Item.objects.filter(visible=1).order_by("name").reverse()

    dept1_items=[]
    dept2_items=[]
    dept3_items=[]
    for items in Item.objects.filter(visible=1):
        for dept in items.department.all():
            if dept == Department.objects.get(id=1):
                dept1_items.append(items)
            if dept == Department.objects.get(id=2):
                dept2_items.append(items)  
            if dept == Department.objects.get(id=3):
                dept3_items.append(items)      
    return render(request, 'home/index.html', {'all_sliders' : sliders,'all_departments' : depatments,'dept1_items':dept1_items,'dept2_items':dept2_items,'dept3_items':dept3_items, 'all_items':all_items})


def depart(request,dept_id):
    depatments = Department.objects.filter(active=1)
    selected_dept = Department.objects.get(id=dept_id)
    selected_items=[]
    for items in Item.objects.filter(visible=1):
        for dept in items.department.all():
            if selected_dept == dept:
                selected_items.append(items)
    return render(request, 'home/depart.html', {'selected_items' : selected_items,'selected_dept':selected_dept,'all_departments' : depatments})

def search(request):
    depatments = Department.objects.filter(active=1)
    s_name= request.POST.get('search_input')
    items = Item.objects.filter(name__contains= s_name)

    return render(request, 'home/search.html', {'items' : items, 'all_departments' : depatments})


def contact(request):
    depatments = Department.objects.filter(active=1)
    template = 'home/contact.html'
    if request.method == 'POST':

        # if request.POST.get('name'):
        #     return render(request, template, {
        #         'error_message': 'Enter your name please.'
        #     })
        # elif request.POST.get('mail'):
        #     return render(request, template, {
        #         'error_message': 'invalid mail .'
        #     })
        # elif request.POST.get('message'):
        #     return render(request, template, {
        #         'error_message': 'enter your message please.'
        #     })
        # else:
        user=Contact.objects.create(
        name= request.POST.get('name')  , mail= request.POST.get('mail') ,
        message=request.POST.get('message')) 
        user.save()
        return render(request, template, {
                'success_message': 'message sent successfully.'
           , 'all_departments' : depatments})
         
    else:
        return render(request, template, {'all_departments' : depatments})

def product(request,item_id):
    depatments = Department.objects.filter(active=1)
    item = Item.objects.get(id=item_id)
    return render(request, 'home/product.html', {'item' : item,'all_departments' : depatments})

def about(request):
    depatments = Department.objects.filter(active=1)
    return render(request, 'home/about.html', {'all_departments' : depatments})

def profile(request):
    return render(request, 'home/profile.html')


def shop(request):
    depatments = Department.objects.filter(active=1)
    items = Item.objects.filter(visible= 1)

    return render(request, 'home/shop.html', {'items' : items, 'all_departments' : depatments})


