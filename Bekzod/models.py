from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="contacts")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post"
        db_table = "posts"

    def __str__(self):
        return self.name


class UserRegisterModel(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserLoginModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username