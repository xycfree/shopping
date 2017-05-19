# coding=utf-8
import json

from django.shortcuts import *
from .models import *
import logging.config
from shop.settings import LOGGING

logging.config.dictConfig(LOGGING)
log = logging.getLogger(__file__)


def login_name(fn):
    def fun(request, *args):
        username = request.session.get('name', default='')
        number = 0
        user = ''

        if username:
            user = UserInfo.objects.get(uName=username)
            number = user.cart_set.filter(isDelete=False).count()  # cart_set （cart）以UserInfo为副键的表
        dic = {
            'user': user,
            'number': number,

        }
        log.info(dic)
        result = fn(request, dic, *args)
        return result

    return fun


def login_yz(fn):
    def fun(request, *args):
        if request.session.has_key('name'):
            result = fn(request, *args)
        else:
            result = redirect('/login/')
        return result

    return fun
