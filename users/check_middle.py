from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

class CheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/':
            return redirect(reverse('blogs:index'))


    # def process_response(self, request, response):
    #     if response.status_code == 404 or response.status_code == 500:
    #         print(response.status_code)
    #         return render(request, '404.html')
