from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.forms import ValidationError
from django.conf import settings

class IITMandiAccountAdapter(DefaultSocialAccountAdapter):
    ''' Adapters for custom IIT Mandi Organization '''

    def pre_social_login(self, request, sociallogin):
        ''' Checks if the user is authorized to create events '''

        # If developer, do not check the condition, simply return
        if settings.DEBUG:
            return

        print("email : ",sociallogin.user.email)
        print(sociallogin.user, type(sociallogin.user))

        emailsplit = sociallogin.user.email.split('@')

        if len(emailsplit) <2:
            raise ValidationError('You are not authorized. Contact Admin.')
        else:    
            email_domain = emailsplit[1].lower()
            email_user = emailsplit[0].lower()
            if 'iitmandi.ac.in' not in email_domain or not email_user.isalpha():
                if '_' not in email_user:
                    raise ValidationError(sociallogin.user.email + ' is not authorized to access Activities. Contact Admin.')
            else:
                pass

