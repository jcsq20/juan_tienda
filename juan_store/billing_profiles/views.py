from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def create(request):
    print("hola desde la vida create")
    return render(request, "billing_profiles/create.html",{

    })