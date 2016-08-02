# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractUser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
    TYPE = (
        (0, '网站用户'),
        (1, '手机用户'),
    )
    auth_user = models.ForeignKey(User, related_name='user_profile')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'姓名')
    telephone = models.CharField(max_length=11, blank=True, null=True, verbose_name=u'手机号')
    type = models.IntegerField(choices=TYPE, verbose_name=u'用户类型', default=0)

    class Meta:
        db_table = 'auth_userprofile'

