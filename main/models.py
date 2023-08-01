from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('DD', 'ДД'),
        ('traders', 'Торговцы'),
        ('gildmaster', 'Гильдмастер'),
        ('questgiver', 'Квестгивер'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастер заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    category = models.CharField(max_length=20, choices=TYPE, default='tank')
    upload = models.ImageField(upload_to='images/', height_field=None, width_field=None,
                               max_length=None, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('fullpost', args=[str(self.id)])

class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
