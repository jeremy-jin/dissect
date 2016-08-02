# -*- coding: utf-8 -*-
from django.test import TestCase

from django.db import transaction
transaction.atomic()

import requests

if __name__ == '__main__':
    data = {
        'username': 'jin19998839',
        'password': 'ttt88888',
        'email': '1234567@qq.com',
        'nickname': 'uuuuuuu'
    }
    req = requests.post('http://127.0.0.1:8080/account/class-base.json', data=data)
    print req
