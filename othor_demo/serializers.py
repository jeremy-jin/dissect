# -*- coding: utf-8 -*-
# author: jeremy


from rest_framework import serializers


class GetAccessTokenSerializer(serializers.Serializer):
    grant_type = serializers.CharField(max_length=30)
    client_id = serializers.CharField(max_length=30)
    client_secret = serializers.CharField(max_length=30)


