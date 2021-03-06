from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField(max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    # 外键关联文章
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]