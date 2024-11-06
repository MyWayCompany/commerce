from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class User(AbstractUser):   
    pass

class Category(models.Model):
    title = models.CharField(max_length=64)
    preview = models.FileField(upload_to="images_categories/")

    def __str__(self) -> str:
        return F"Категория: {self.title}"

class Comment(models.Model):
    text = models.CharField(max_length=500)
    dateTime_creation = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self) -> str:
        return F"Комментарий полязователя: {self.user.username}"

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Listing(models.Model):    
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    start_price = models.IntegerField()
    dateTime_creation = models.DateTimeField()   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_user")    
    users =  models.ManyToManyField(User, related_name="watch_listing", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", blank=True)
    comment = models.ManyToManyField(Comment, null=True, blank=True, related_name="comments")
    preview = models.FileField(upload_to=user_directory_path)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return F"Объявление: {self.title}, пользователя: {self.user.username}"
