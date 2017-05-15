from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]


    '''这里我们会记录评论用户的 name（名字）、email（邮箱）、url（个人网站），
    用户发表的内容将存放在 text 字段里，created_time 记录评论时间。最后，这
    个评论是关联到某篇文章（Post）的，由于一个评论只能属于一篇文章，一篇文章
    可以有多个评论，是一对多的关系，因此这里我们使用了 ForeignKey。关于 ForeKey
    的只是我们前面已有介绍。'''