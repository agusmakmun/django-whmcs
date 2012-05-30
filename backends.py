from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from api import WHMCS
from models import UserProfile

class AccountBackend (object):

    whmcs = WHMCS()

    def try_whmcs (self, username, password):
        client = self.whmcs.client_get_set(0, 1, username)
        
        if len(client) == 0:
            return self.authenticate(username, password, False)

        client = client[0]

        # let's make the user object

        user = User.objects.create_user(
                    username,
                    username,
                    password
        )
        user.save()
        (password, salt) = self.whmcs.client_get_password(client.id)
        profile = UserProfile.objects.create(
                    user=user,
                    whmcs_id=client.id,
                    salt=salt,
                    last_password=password
        )
        profile.save()

        return self.authenticate(username, password, False)

    def validate_email (self, username):

        try:
            validate_email(username)
            return True
        except ValidationError:
            return False

    def authenticate (self, username=None, password=None, first_attempt=True):

        if not self.validate_email(username):
            return None

        try:
            user = User.objects.get(email=username)

        except User.DoesNotExist:
            if first_attempt: 
                return self.try_whmcs(username, password)
            else:
                return None

        # now we have our user, check if the password is valid
        if self.whmcs.client_check_password(user.get_profile().whmcs_id, password):
            return user       

        return None

    def get_user (self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None





