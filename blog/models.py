from django.db import models
from django.conf import settings


class Blog(models.Model):
    user_id = models.IntegerField()
    owner = models.CharField(max_length=30, default="???")
    image = models.ImageField(upload_to="sns/%Y/%m/%d")  # 어디에 업로드할지 지정할 수 있음.
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def increaseViews(self):
        self.views +=1
        self.save()


class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text
