from django.shortcuts import render

from django.http import HttpResponse

# This will be the index where all of the users are listed
# Option to add user
def index(request):
    return HttpResponse("Index page")

# TODO: Query for the user from database
# Send context to render
def edit_user(request, user_id):
    return HttpResponse(F"Edit user page {user_id}")
