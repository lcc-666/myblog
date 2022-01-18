from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render

class CheckMiddleware(MiddlewareMixin):


    def process_response(self, request, response):
        if response.status_code == 404 or response.status_code == 500:
            print(response.status_code)
            return render(request, '404.html')
