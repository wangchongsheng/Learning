# @Time    : 2018/2/22 0022 15:22
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : my_tag.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register是固定变量名，不能改变

#不能用于if语句
@register.simple_tag
def my_add100(v1, v2, v3):
    return v1 + 100 + v2 + v3



#filter的参数不能超过两个
@register.filter
def my_add100(v1, v2):
    return v1 + v2

