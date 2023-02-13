from django.db import models
from xml.dom import ValidationErr
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Person(User):
    cin = models.CharField(primary_key=True, max_length=8)
    mail = models.EmailField()
    def validemail(self):
        if not self.mail.endswith('@esprit.tn'):
            raise ValidationErr('Email {mail} must end with @esprit.tn ',params={"email":self.mail})  
    class Meta:
        db_table = 'Person'
