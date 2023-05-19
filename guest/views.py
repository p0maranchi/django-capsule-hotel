from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse_lazy 
from .forms import UserPasswordChangeForm 

def loginUser(request):
    if request.method == "POST":
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            ...
            messages.error(request, "Неправильний логін або пароль")
            return redirect('login')
        
    else:
        return render(request, 'authenticate/login.html', {

        })

def logoutUser(request):
    logout(request)
    messages.success(request, "Ви вийшли")
    return redirect('index')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Паролі не співпадають!")
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "Реєстрацію завершено!")
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register.html', {
        'form':form,
    })

class UserPasswordChange(SuccessMessageMixin, PasswordChangeView): 
  
    form_class = UserPasswordChangeForm 
    template_name = 'authenticate/user_password_change.html' 
    success_message = 'Ваш пароль змінено!' 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        return context 
 
    def get_success_url(self): 
        return reverse_lazy('userPanel')