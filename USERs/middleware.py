from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

CHECK_URL = ['/usercreate/','/userlist/']
IP = "127.0.0.1"

class Ipcheck:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        request_url = request.path_info
        request_ip = request.META['REMOTE_ADDR']

        #print(request_ip,request_url)

        if request_url in CHECK_URL:
            if request_ip == IP:
                return None

            return JsonResponse({'Message': 'Permission Denied'},  status=status.HTTP_201_CREATED)



