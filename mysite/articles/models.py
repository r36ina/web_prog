from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='image/', blank=True, default='default.jpg')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50] + '...'