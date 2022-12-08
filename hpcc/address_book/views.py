from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import User

def index(request):
    users = User.objects.all()
    return render(request, 'address_book/index.html', { 'users': users })


def edit_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect("/")
    
    ctxt = { 'user' : user } 
    return render(request, "address_book/edit_user.html", context=ctxt)


def edit_user_modify(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        
        user.first_name = request.POST['user_first_name']
        user.last_name = request.POST['user_last_name']
        user.phone_number = request.POST['user_phone_number']
        
        user.address.number = request.POST['address_number']
        user.address.street_name = request.POST['address_street_name']
        user.address.apt = request.POST['address_apt']
        user.address.zip_code = request.POST['address_zip_code']
        user.address.city = request.POST['address_city']
        user.address.state = request.POST['address_state']
        
        user.save()
        return HttpResponseRedirect(reverse("addr_book:edit", args=(user.pk,)))
        
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("addr_book:index"))
