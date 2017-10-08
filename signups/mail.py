
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

class MailSender(object):

    def get_signup_message(self, save_it):
        self.signup_message =  'Hello ' + save_it.first_name + ', '\
                      ' \n\n Thanks for taking the time to look around the algorithm demo website.' \
                       ' Let me know of any feed back you have and how I can make the website better.'  \
                      ' If you would like to reach me just reply to this email and I will get back to you promptly. ' \
                       '\n\n Thank you and have a good day!'\
                      '\n\n Michael Scotto\n Web Developer\nNew York City Metropolitan Area\n\n'


    def send_mail_to_signup(self, form, request):
      if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            messages.success(request, 'We will be in touch.')
            subject='Thank you for taking a look at our website'
            message = self.get_sign_up_message(save_it)
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)