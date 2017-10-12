from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


class MailSender(object):
    def get_signup_message(self, first_name):
        signup_message = 'Hello ' + first_name + ', ' \
        ' \n\n Thanks for taking the time to look around the algorithm demo website.' \
        ' Let me know of any feed back you have and how I can make the website better.' \
        ' If you would like to reach me just reply to this email and I will get back to you promptly. ' \
        '\n\n Thank you and have a good day!' \
        '\n\n Michael Scotto\n Web Developer\nNew York City Metropolitan Area\n\n'
        return signup_message

    def send_mail_to_signup(self, request, first_name, email):
        messages.success(request, 'We will be in touch.')
        subject = 'Thank you for taking a look at our website'
        message = self.get_signup_message(first_name)
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
