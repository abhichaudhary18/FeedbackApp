from django.db import models
from django.contrib import auth
import uuid
from django.core.exceptions import ValidationError
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

def validate_image(image):
    file_size = image.file.size
    limit_kb = 50
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

class Sendmessage(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    username =models.CharField(max_length=150)
    message = models.TextField(max_length=1500)
    meme = models.ImageField(upload_to='media',blank=True , null=True,validators=[validate_image])
    date = models.DateTimeField(auto_now_add=True)
    class meta():
        db_table ='message received'
