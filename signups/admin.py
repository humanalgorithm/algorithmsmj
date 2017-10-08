from django.contrib import admin



from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        fields = "__all__"

admin.site.register(SignUp, SignUpAdmin)
