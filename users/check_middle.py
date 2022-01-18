from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

class CheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/':
            return redirect(reverse('blogs:index'))

