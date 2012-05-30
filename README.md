django-whmcs
============

A Django app to provide integration with [.WHMCS](http://www.whmcs.com/).

Installation
-----------

Add the following to your settings.py:

AUTHENTICATION_BACKENDS = (                                                     
    'whmcs.backends.AccountBackend',                                       
    'django.contrib.auth.backends.ModelBackend',                                
)                                                                               
                                                                                                                                                               
AUTH_PROFILE_MODULE = 'whmcs.UserProfile'         

from libs.whmcs.settings import *                                               

Credits
-------

Forked from: [.robrocker7](https://github.com/robrocker7/whmcs)
