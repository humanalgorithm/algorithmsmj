from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from .forms import SignUpForm
from rest_framework import generics
from models import SignUp
from serializers import SignUpSerializer
from mail import MailSender


def signup(request):
  form = SignUpForm(request.POST or None)
  MailSender().send_mail_to_signup(form, request)
  return HttpResponseRedirect('/thank-you/')


def thankyou(request):
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance =RequestContext(request))

class SignUpList(generics.ListCreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

