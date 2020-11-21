from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    if request.method == 'POST':

        #https://support.google.com/accounts/answer/6010255
        from django.conf import settings

        from django.core.mail import send_mail

        print("Sending Email"
        )


        from django.core.mail import send_mail

        a=send_mail('Mail Subject', 'Mail content', settings.EMAIL_HOST_USER, ['to@info@check-point.us'], fail_silently=True)

        print("Email Sent")
    context = { 'a': 0}
    return render(request, 'content/index.html', context)



@csrf_exempt
def send_email(request):

    #https://support.google.com/accounts/answer/6010255
    from django.conf import settings

    from django.core.mail import send_mail

    print("Sending Email"
    )


    from django.core.mail import send_mail

    a=send_mail('Mail Subject', 'Mail content', settings.EMAIL_HOST_USER, ['info@check-point.us', 'aiden3189@gmail.com'], fail_silently=False)

    print("Email Sent", a)

    return HttpResponse('ok')

def about(request):
    context = { 'a': 0}
    return render(request, 'content/about.html', context)


def contact(request):
    context = { 'a': 0}
    return render(request, 'content/contact.html', context)