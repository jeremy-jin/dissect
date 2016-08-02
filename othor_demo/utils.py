# -*- coding: utf-8 -*-
# author: jeremy
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

GET_ACCESS_TOKEN_URL = 'https://graph.qq.com/oauth2.0/token?'


class TokenCallbackAPIView(APIView):
    """"""
    def get(self, request):
        pass

