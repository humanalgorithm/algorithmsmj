from django.shortcuts import render, HttpResponseRedirect
from rest_framework import generics
from models import SignUp
from serializers import SignUpSerializer
from mail import MailSender
from email.utils import parseaddr
from django.views.generic.base import View
from .models import SignUp
from django.contrib import messages

class SignUpView(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        print request.POST

        if first_name and last_name and self.valid_email(email):
            SignUp.objects.create(first_name=first_name, last_name=last_name, email=email)
            MailSender().send_mail_to_signup(request, first_name, email)
            messages.success(request, 'You have successfully signed up and will receive an email.')
            return render(request, "page/thankyou.html")
        else:
            if not first_name:
                messages.error(request, "Please provide a first name")
            if not last_name:
                messages.error(request, "Please provide a last name")
            if not self.valid_email(email):
                messages.error(request, "Please provide a valid email")
            return render(request, "page/thankyou.html")


    def valid_email(self, email):
        return '@' in parseaddr(email)[1]


class SignUpList(generics.ListCreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
