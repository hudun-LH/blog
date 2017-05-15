# -*- coding:utf-8 -*-

from django import template

from ..models import Post,Category

register = template.Library()

@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all()[:num]



@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')



'''这个 dates 方法会返回一个列表，列表中的元素为每一篇 Post 创建的时间
，精确到月份，降序排列。接受的三个参数值表明了这些含义，一个是 created_time ，
即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列。例如如果我们
写了 3 篇文章，分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、2017 年 3
 月 28 日，那么 date 将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，从
 而帮助我们实现按月归档的目的。'''





@register.simple_tag
def get_categories():
    return Category.objects.all()