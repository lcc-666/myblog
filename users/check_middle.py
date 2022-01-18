from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class CheckMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        #print(response.status_code)
        print('4554')


