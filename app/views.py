from django.shortcuts import render
from .models import CustomerData, OrderDetails
from .forms import Login, Signup
from django.shortcuts import redirect



def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = CustomerData.objects.filter(email=email, password=password)
        if customer:
            return redirect('index')
        else:
            return redirect('login')

    form = Login()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        customer = CustomerData(name=name, email=email, phone=phone, password=password)
        customer.save()
        return redirect('login')


    form = Signup()
    return render(request, 'signup.html', {'form': form})
