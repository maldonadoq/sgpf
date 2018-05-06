from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.db import models

# Create your models here.
class UserType(models.Model):
    type = models.CharField(max_length=20)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.type


# User class that will be mapped in the database as a table. [mycash_user]
class User(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)   # fk to pk of user type
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=20)                              # user name
    last_name = models.CharField(max_length=50)                         # user last name
    email = models.CharField(max_length=50)                             # user email
    phone = models.CharField(max_length=12)                             # user phone optional
    state = models.BooleanField(default=True)                           # user state [delete]

    def __str__(self):                                                  # print
        cad = "{0} {1}, {2}"
        return cad.format(self.name, self.last_name, self.email)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    number_credits = models.IntegerField()

    def __unicode__(self):
        return u'{}'.format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_student = models.ManyToManyField(Subject)

    def full_name(self):
        return u'{} {}'.format(self.name, self.last_name)