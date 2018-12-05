# -*- coding:utf8 -*-
from django.db import models


# Create your models here.
class User(models.Model):
    """
    用户表
    """

    name = models.CharField(max_length=128)
    account = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    credit = models.IntegerField(null=True)
    mobile_number = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    img_src = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Shop(models.Model):
    """
    商铺表
    """

    shop_owner = models.IntegerField()


class Goods(models.Model):
    """
    商品表
    """
    name = models.CharField(max_length=256, default="")
    shop_id = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    validity = models.BooleanField()
    detail = models.CharField(max_length=256)
    category = models.CharField(max_length=256)


class UserFavourites(models.Model):
    """
    收藏夹
    """
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)


# class Order(models.Model):
#     """
#     订单表
#     """
#
#     submit_time = DateTimeField(auto_now_add=True)
#     shop_id = models.IntegerField()
#     goods_id = models.IntegerField()
#     status = models.IntegerField()  # 0 卖家未确认， 1 卖家确认，订单正在进行， 2 订单完成



