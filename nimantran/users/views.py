from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        phone_number = request.POST['phoneNumber']
        email = request.POST['emailId']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        if password != confirm_password:
            raise Exception("Password does not match")
        user = User(full_name=full_name, phone_number=phone_number, email=email)
        user.set_password(password)
        user.save()
        return HttpResponse(full_name)
    else:
        return render(request, "index.html")