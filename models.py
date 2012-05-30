from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.ForeignKey(User, unique=True)
    whmcs_id = models.IntegerField()
    salt = models.CharField(max_length=10)
    last_password = models.CharField(max_length=200)    

    def __str__ (self):
        return '%s whmcs: %d' % (self.user.username, self.whmcs_id)

class UserBrowser (models.Model):
    name = models.CharField(max_length=200)

class UserLogin (models.Model):
    user = models.ForeignKey(UserProfile)
    time = models.DateTimeField(auto_now_add=True)
    address = models.GenericIPAddressField()
    browser = models.ForeignKey(UserBrowser)

