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
        user = User.objects.get(username=username)
        if user.check_password(password):
            auth.login(request,user)
            request.session['status'] = 1
            return redirect(reverse('blogs:article'))
        else:
            return render(request, 'login.html')