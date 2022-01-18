from django.shortcuts import redirect
from django.urls import reverse
import re
from django.utils.deprecation import MiddlewareMixin


# class ShopMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#         path=request.path
#         print(path)
#         print(request.session['status'])
#         if re.match(r'^/blogs', path):
#             if request.session['status'] == 1:
#                 print('544545')



