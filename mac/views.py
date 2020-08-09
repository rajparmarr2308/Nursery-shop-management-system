from django.shortcuts import render
from shop.forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
def index(request):
    return render(request, 'index.html')

def Userlogin(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/shop')
        else:
            data['error'] = "Username or Password is incorrect"
            res = render(request, 'login.html', data)
            return res
    else:
        return render(request, 'login.html', data)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})        

       