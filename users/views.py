from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('logname')
        password=request.POST.get('logpass')
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'login.html', context={'data': '用户名或密码错误'})
        if user.check_password(password):
            auth.login(request,user)
            request.session['status'] = 1
            return redirect(reverse('blogs:article'))
        else:
            return render(request, 'login.html',context={'data':'用户名或密码错误'})

class LogoutView(View):
    def get(self,request):
        request.session['status']=0
        return redirect(reverse('blogs:index'))